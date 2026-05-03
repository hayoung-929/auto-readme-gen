"""프로젝트 분석 모듈 - 확장 버전"""
import os
import json
import re
from pathlib import Path
from collections import Counter
import git

# os.walk 시 하위 디렉터리 제외: 의존성·캐시·빌드 산출물
# 'auto-readme-gen': 워크스페이스 상위 폴더를 분석할 때 옆에 둔 이 도구 클론이 본 프로젝트 통계에 섞이지 않도록
SKIP_SUBDIRS = frozenset({
    ".git",
    "venv",
    ".venv",
    "node_modules",
    "__pycache__",
    ".vscode",
    "dist",
    "build",
    ".eggs",
    ".tox",
    ".mypy_cache",
    "htmlcov",
    ".pytest_cache",
    "auto-readme-gen",
})


def read_file_safely(file_path, max_lines=50):
    """
    파일을 안전하게 읽기 (에러 처리, 라인 제한)
    
    Args:
        file_path: 읽을 파일 경로
        max_lines: 최대 읽을 라인 수
        
    Returns:
        str: 파일 내용 또는 None
    """
    try:
        with open(file_path, 'r', encoding='utf-8') as f:
            lines = []
            for i, line in enumerate(f):
                if i >= max_lines:
                    break
                lines.append(line)
            return ''.join(lines)
    except:
        return None


def extract_requirements(project_path):
    """requirements.txt 파싱"""
    req_file = Path(project_path) / 'requirements.txt'
    if not req_file.exists():
        return []
    
    content = read_file_safely(req_file)
    if not content:
        return []
    
    packages = []
    for line in content.split('\n'):
        line = line.strip()
        if line and not line.startswith('#'):
            # flask==2.0.1 -> flask
            package = line.split('==')[0].split('>=')[0].split('<=')[0].strip()
            packages.append(package.lower())
    
    return packages


def extract_package_json(project_path):
    """package.json 파싱"""
    pkg_file = Path(project_path) / 'package.json'
    if not pkg_file.exists():
        return {}
    
    content = read_file_safely(pkg_file)
    if not content:
        return {}
    
    try:
        data = json.loads(content)
        return {
            'name': data.get('name', ''),
            'scripts': data.get('scripts', {}),
            'dependencies': list(data.get('dependencies', {}).keys())
        }
    except:
        return {}


def extract_cli_command(project_path):
    """
    setup.py에서 CLI 명령어 추출
    
    Args:
        project_path: 프로젝트 경로
        
    Returns:
        str: CLI 명령어 이름 또는 None
    """
    setup_file = Path(project_path) / 'setup.py'
    if not setup_file.exists():
        return None
    
    content = read_file_safely(setup_file, max_lines=100)
    if not content:
        return None
    
    # entry_points에서 console_scripts 찾기
    # 예: 'readme-gen = readme_gen.cli:cli'
    pattern = r"'([^']+)\s*=\s*[^']+:cli'"
    matches = re.findall(pattern, content)
    
    if matches:
        return matches[0]  # 첫 번째 명령어
    
    # 대체 패턴 (console_scripts 형식)
    pattern2 = r'"([^"]+)\s*=\s*[^"]+:cli"'
    matches2 = re.findall(pattern2, content)
    
    if matches2:
        return matches2[0]
    
    return None


def detect_framework(project_info, packages):
    """
    프레임워크 자동 감지
    
    Args:
        project_info: 프로젝트 정보
        packages: requirements.txt의 패키지 목록
        
    Returns:
        str: 감지된 프레임워크
    """
    packages_lower = [p.lower() for p in packages]
    
    # Python 프레임워크
    if 'flask' in packages_lower:
        return 'Flask'
    elif 'django' in packages_lower:
        return 'Django'
    elif 'fastapi' in packages_lower:
        return 'FastAPI'
    elif 'streamlit' in packages_lower:
        return 'Streamlit'
    
    # JavaScript 프레임워크 (package.json 기반)
    pkg_json = project_info.get('package_json', {})
    deps = pkg_json.get('dependencies', [])
    deps_lower = [d.lower() for d in deps]
    
    if 'react' in deps_lower:
        return 'React'
    elif 'vue' in deps_lower:
        return 'Vue.js'
    elif 'express' in deps_lower:
        return 'Express.js'
    elif 'next' in deps_lower:
        return 'Next.js'
    
    return None


def detect_project_type(project_info):
    """
    프로젝트 타입 감지
    
    Args:
        project_info: 프로젝트 정보
        
    Returns:
        str: 'cli_tool', 'web_app', 'library', 'script'
    """
    # CLI 도구 체크
    if project_info.get('cli_command'):
        return 'cli_tool'
    
    # 웹 프레임워크 체크
    framework = project_info.get('framework')
    if framework in ['Flask', 'Django', 'FastAPI', 'Express.js', 'React', 'Vue.js', 'Next.js']:
        return 'web_app'
    
    # setup.py 있으면 라이브러리 가능성
    if (Path(project_info['path']) / 'setup.py').exists():
        return 'library'
    
    return 'script'


def find_entry_points(project_path):
    """
    프로젝트 엔트리 포인트 찾기
    
    Returns:
        list: 발견된 엔트리 파일 목록
    """
    path = Path(project_path)
    entry_files = []
    
    # 일반적인 엔트리 포인트 파일명
    common_entries = [
        'main.py', 'app.py', 'run.py', 'manage.py',
        'index.js', 'server.js', 'app.js', 'main.js',
        'index.html', 'index.tsx', 'index.ts'
    ]
    
    for entry in common_entries:
        if (path / entry).exists():
            entry_files.append(entry)
    
    return entry_files


def extract_dockerfile_info(project_path):
    """Dockerfile에서 실행 정보 추출"""
    dockerfile = Path(project_path) / 'Dockerfile'
    if not dockerfile.exists():
        return None
    
    content = read_file_safely(dockerfile, max_lines=30)
    if not content:
        return None
    
    info = {
        'has_dockerfile': True,
        'expose_ports': [],
        'cmd': None
    }
    
    for line in content.split('\n'):
        line = line.strip()
        if line.startswith('EXPOSE'):
            port = line.split('EXPOSE')[1].strip()
            info['expose_ports'].append(port)
        elif line.startswith('CMD'):
            info['cmd'] = line.split('CMD')[1].strip()
    
    return info


def get_git_info(project_path):
    """
    Git 정보 추출 (GitHub URL, 사용자명 등)
    
    Args:
        project_path: 프로젝트 경로
        
    Returns:
        dict: Git 정보 또는 None
    """
    try:
        repo = git.Repo(project_path, search_parent_directories=True)
        
        if 'origin' in repo.remotes:
            remote_url = repo.remotes.origin.url
            
            if 'github.com' in remote_url:
                if remote_url.startswith('git@'):
                    remote_url = remote_url.replace('git@github.com:', 'https://github.com/')
                
                remote_url = remote_url.rstrip('.git')
                
                parts = remote_url.split('github.com/')
                if len(parts) == 2:
                    user_repo = parts[1]
                    username = user_repo.split('/')[0]
                    repo_name = user_repo.split('/')[1] if '/' in user_repo else ''
                    
                    return {
                        'has_git': True,
                        'remote_url': remote_url,
                        'username': username,
                        'repo_name': repo_name,
                        'clone_url': f"{remote_url}.git"
                    }
        
        return {'has_git': True}
    
    except (git.InvalidGitRepositoryError, git.GitCommandError):
        return {'has_git': False}


def analyze_project(project_path):
    """
    프로젝트 디렉토리를 분석해서 정보 추출 (확장 버전)
    
    Args:
        project_path: 분석할 프로젝트 경로
        
    Returns:
        dict: 프로젝트 정보 (이름, 언어, 파일 개수, 프레임워크, 엔트리포인트 등)
    """
    
    # 절대 경로로 변환
    path = Path(project_path).resolve()
    
    # 경로 존재 확인
    if not path.exists():
        raise ValueError(f"경로를 찾을 수 없습니다: {project_path}")
    
    if not path.is_dir():
        raise ValueError(f"디렉토리가 아닙니다: {project_path}")
    
    # 기본 정보 딕셔너리
    project_info = {
        'name': path.name,
        'path': str(path.absolute()),
        'languages': [],
        'file_count': 0,
        'has_docker': False,
        'has_requirements': False,
        'has_package_json': False,
    }
    
    # 파일 확장자별 개수 세기
    extensions = Counter()
    
    # 디렉토리 전체 탐색
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in SKIP_SUBDIRS]
        
        for file in files:
            project_info['file_count'] += 1
            ext = Path(file).suffix
            
            # 확장자가 있으면 카운트
            if ext:
                extensions[ext] += 1
            
            # 특정 파일 체크
            if file == 'Dockerfile':
                project_info['has_docker'] = True
            elif file == 'requirements.txt':
                project_info['has_requirements'] = True
            elif file == 'package.json':
                project_info['has_package_json'] = True
    
    # 확장자로 언어 판별
    lang_map = {
        '.py': 'Python',
        '.js': 'JavaScript',
        '.ts': 'TypeScript',
        '.go': 'Go',
        '.rs': 'Rust',
        '.java': 'Java',
        '.cpp': 'C++',
        '.c': 'C',
        '.rb': 'Ruby',
        '.php': 'PHP',
    }
    
    # 가장 많이 쓰는 언어 3개 추출
    for ext, count in extensions.most_common(3):
        if ext in lang_map:
            project_info['languages'].append(lang_map[ext])
    
    # 확장자 정보도 저장
    project_info['extensions'] = dict(extensions)
    
    # === 확장 분석 시작 ===
    
    # 1. requirements.txt 파싱
    packages = extract_requirements(project_path)
    project_info['packages'] = packages
    
    # 2. package.json 파싱
    pkg_json = extract_package_json(project_path)
    project_info['package_json'] = pkg_json
    
    # 3. 프레임워크 감지
    framework = detect_framework(project_info, packages)
    project_info['framework'] = framework
    
    # 4. 엔트리 포인트 찾기
    entry_points = find_entry_points(project_path)
    project_info['entry_points'] = entry_points
    
    # 5. Dockerfile 정보
    dockerfile_info = extract_dockerfile_info(project_path)
    if dockerfile_info:
        project_info['dockerfile'] = dockerfile_info
    
    # 6. CLI 명령어 추출
    cli_command = extract_cli_command(project_path)
    if cli_command:
        project_info['cli_command'] = cli_command
    
    # 7. 프로젝트 타입 감지
    project_type = detect_project_type(project_info)
    project_info['project_type'] = project_type
    
    # === 확장 분석 끝 ===
    
    # Git 정보 추가
    git_info = get_git_info(project_path)
    project_info['git'] = git_info
    
    # 빈 프로젝트 체크
    if project_info['file_count'] == 0:
        project_info['is_empty'] = True
    else:
        project_info['is_empty'] = False
    
    # 언어를 하나도 못 찾았으면 기본값
    if not project_info['languages']:
        project_info['languages'] = ['Unknown']
    
    return project_info


# 테스트용 코드
if __name__ == '__main__':
    result = analyze_project('.')
    
    print("=" * 50)
    print("프로젝트 분석 결과:")
    print("=" * 50)
    for key, value in result.items():
        print(f"{key}: {value}")