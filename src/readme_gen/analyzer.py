"""프로젝트 분석 모듈"""
import os
from pathlib import Path
from collections import Counter
import git


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
    프로젝트 디렉토리를 분석해서 정보 추출
    
    Args:
        project_path: 분석할 프로젝트 경로
        
    Returns:
        dict: 프로젝트 정보 (이름, 언어, 파일 개수 등)
    """
    
    path = Path(project_path).resolve()
    
    project_info = {
        'name': path.name,
        'path': str(path.absolute()),
        'languages': [],
        'file_count': 0,
        'has_docker': False,
        'has_requirements': False,
        'has_package_json': False,
    }
    
    extensions = Counter()
    
    for root, dirs, files in os.walk(path):
        dirs[:] = [d for d in dirs if d not in ['.git', 'venv', 'node_modules', '__pycache__', '.vscode']]
        
        for file in files:
            project_info['file_count'] += 1
            ext = Path(file).suffix
            
            if ext:
                extensions[ext] += 1
            
            if file == 'Dockerfile':
                project_info['has_docker'] = True
            elif file == 'requirements.txt':
                project_info['has_requirements'] = True
            elif file == 'package.json':
                project_info['has_package_json'] = True
    
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
    
    for ext, count in extensions.most_common(3):
        if ext in lang_map:
            project_info['languages'].append(lang_map[ext])
    
    project_info['extensions'] = dict(extensions)
    
    # Git 정보 추가 (여기!)
    git_info = get_git_info(project_path)
    project_info['git'] = git_info
    
    return project_info


if __name__ == '__main__':
    result = analyze_project('.')
    
    print("=" * 50)
    print("프로젝트 분석 결과:")
    print("=" * 50)
    for key, value in result.items():
        print(f"{key}: {value}")