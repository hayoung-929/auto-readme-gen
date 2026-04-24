"""AI 기반 프로젝트 README 생성"""
import os
import json
import google.generativeai as genai


def generate_readme_with_ai(project_info):
    """
    Gemini AI로 README의 주요 섹션 전체 생성
    
    Args:
        project_info: analyzer에서 추출한 프로젝트 정보
        
    Returns:
        dict: AI가 생성한 README 섹션들
    """
    
    # API 키 확인
    api_key = os.getenv('GEMINI_API_KEY')
    if not api_key:
        raise ValueError(
            "GEMINI_API_KEY 환경변수가 설정되지 않았습니다.\n"
            "https://ai.google.dev 에서 API 키를 발급받아 설정하세요.\n"
            "예: export GEMINI_API_KEY='your-api-key'"
        )
    
    # Gemini 설정
    genai.configure(api_key=api_key)
    model = genai.GenerativeModel('gemini-2.5-flash')
    
    # 프로젝트 정보 준비
    framework_info = project_info.get('framework', 'None')
    packages = project_info.get('packages', [])[:10]
    entry_points = project_info.get('entry_points', [])
    pkg_json = project_info.get('package_json', {})
    scripts = pkg_json.get('scripts', {})
    dockerfile_info = project_info.get('dockerfile', {})
    cli_command = project_info.get('cli_command', 'None')
    project_type = project_info.get('project_type', 'script')
    
    # 프롬프트
    context = f"""
당신은 전문 개발자이자 기술 문서 작성 전문가입니다.
다음 프로젝트 정보를 분석하여 README의 주요 섹션들을 JSON 형식으로 생성해주세요.

## 프로젝트 분석 정보

### 기본 정보
- 프로젝트명: {project_info['name']}
- 주 언어: {project_info['languages'][0] if project_info['languages'] else 'Unknown'}
- 사용 언어: {', '.join(project_info['languages'])}
- 총 파일 수: {project_info['file_count']}

### 기술 스택
- 프레임워크: {framework_info}
- 주요 패키지: {', '.join(packages) if packages else 'None'}
- 엔트리 포인트: {', '.join(entry_points) if entry_points else 'None'}
- npm scripts: {', '.join(scripts.keys()) if scripts else 'None'}

### 실행 환경
- **프로젝트 타입: {project_type}**
- **CLI 명령어 이름: {cli_command}**
- Docker 컨테이너화: {'있음' if project_info['has_docker'] else '없음'}
- requirements.txt: {'있음' if project_info['has_requirements'] else '없음'}
- package.json: {'있음' if project_info['has_package_json'] else '없음'}
{f"- 노출 포트: {', '.join(dockerfile_info.get('expose_ports', []))}" if dockerfile_info.get('expose_ports') else ''}

### Git 정보
- 저장소명: {project_info.get('git', {}).get('repo_name', '없음')}

## 작성 요구사항

다음 형식의 JSON을 생성해주세요. **반드시 유효한 JSON 형식**으로, 마크다운 코드블록 없이 순수 JSON만 출력하세요:

{{
  "description": "프로젝트 설명 (2-3문장, 간결하고 기술적으로 정확하게)",
  "features": [
    "주요 기능 1",
    "주요 기능 2",
    "주요 기능 3",
    "주요 기능 4"
  ],
  "installation_steps": [
    "설치 단계 1 (명령어 포함)",
    "설치 단계 2",
    "설치 단계 3"
  ],
  "run_command": "실행 명령어 (정확한 명령어 하나)",
  "run_description": "실행 방법 설명 (1-2문장)",
  "usage_examples": [
    "사용 예시 1 (명령어 + 설명)",
    "사용 예시 2"
  ]
}}

## 구체적인 지침

### description
- 프레임워크와 주요 기술 스택 반드시 언급
- 무엇을 하는 프로젝트인지 명확히
- "이 프로젝트는" 같은 시작 제거

### features
- 분석된 정보에 기반한 실제 기능
- 4-6개 항목
- 구체적으로 (예: "사용자 인증 기능", "Docker 컨테이너화 지원")

### installation_steps
- 프레임워크에 맞는 정확한 설치 방법
- Flask/Django → venv 생성, pip install -r requirements.txt
- Node.js → npm install 또는 yarn install
- **CLI 도구 (project_type='cli_tool') → pip install 또는 pip install -e .**
- 3-5단계로 간결하게

### run_command
- **단 하나의 정확한 명령어**
- **CRITICAL: CLI 도구인 경우 (project_type='cli_tool'): 반드시 CLI 명령어 이름을 사용하세요!**
  - CLI 명령어가 '{cli_command}'인 경우 → "{cli_command} [적절한 서브커맨드]"
  - 절대 "python cli.py" 같은 형식 사용 금지!
- Flask → "flask run" 또는 "python app.py"
- Django → "python manage.py runserver"
- FastAPI → "uvicorn main:app --reload"
- Node.js → "npm start" 또는 "npm run dev"
- React/Vue → "npm run dev"
- 엔트리 포인트({', '.join(entry_points)})를 참고하여 결정

### run_description
- 실행 후 어떻게 되는지 (예: "개발 서버가 http://localhost:3000에서 실행됩니다")
- 추가 옵션이나 팁

### usage_examples
- 실제 사용 시나리오 2-3개
- 명령어 + 간단한 설명
- CLI 도구라면 주요 서브커맨드들 (예: analyze, generate 등)
- 웹앱이라면 주요 엔드포인트나 기능

## 예시

Django 프로젝트 (project_type='web_app'):
{{
  "description": "Django와 PostgreSQL을 사용하는 블로그 웹 애플리케이션입니다. 사용자 인증, 게시글 CRUD, 댓글 기능을 제공하며 Django REST Framework로 API를 구현했습니다.",
  "features": [
    "사용자 회원가입 및 로그인 기능",
    "게시글 작성, 수정, 삭제",
    "댓글 및 답글 시스템",
    "REST API 제공",
    "관리자 페이지"
  ],
  "installation_steps": [
    "가상환경 생성: python -m venv venv",
    "가상환경 활성화: source venv/bin/activate (Windows: venv\\\\Scripts\\\\activate)",
    "패키지 설치: pip install -r requirements.txt",
    "데이터베이스 마이그레이션: python manage.py migrate"
  ],
  "run_command": "python manage.py runserver",
  "run_description": "개발 서버가 http://127.0.0.1:8000 에서 실행됩니다. 관리자 페이지는 /admin 경로에서 접근 가능합니다.",
  "usage_examples": [
    "슈퍼유저 생성: python manage.py createsuperuser",
    "정적 파일 수집: python manage.py collectstatic"
  ]
}}

CLI 도구 프로젝트 (project_type='cli_tool', cli_command='readme-gen'):
{{
  "description": "Python Click 프레임워크 기반의 README 자동 생성 CLI 도구입니다. 프로젝트를 분석하여 Git 정보, 언어, 프레임워크를 자동 감지하고 전문적인 README를 생성합니다.",
  "features": [
    "프로젝트 자동 분석 (언어, 프레임워크, Git 정보)",
    "AI 기반 프로젝트 설명 생성",
    "한글/영어 템플릿 지원",
    "대화형 CLI 인터페이스",
    "커스텀 템플릿 지원"
  ],
  "installation_steps": [
    "저장소 복제 및 이동: git clone <repo> && cd <project>",
    "가상환경 생성: python -m venv venv",
    "가상환경 활성화: source venv/bin/activate (Windows: venv\\\\Scripts\\\\activate)",
    "개발 모드 설치: pip install -e ."
  ],
  "run_command": "readme-gen generate .",
  "run_description": "현재 디렉토리의 프로젝트를 분석하여 README.md 파일을 생성합니다. --ai 옵션으로 AI 기반 설명을 추가할 수 있습니다.",
  "usage_examples": [
    "프로젝트 분석만 수행: readme-gen analyze .",
    "AI 기반 생성: readme-gen generate . --ai",
    "영어 버전 생성: readme-gen generate . --lang english"
  ]
}}

React 프로젝트 (project_type='web_app'):
{{
  "description": "React와 TypeScript 기반의 대시보드 애플리케이션입니다. Chart.js를 활용한 데이터 시각화와 반응형 디자인을 제공하며, Vite로 빠른 개발 환경을 구축했습니다.",
  "features": [
    "실시간 데이터 시각화",
    "반응형 대시보드 UI",
    "TypeScript 타입 안정성",
    "Vite를 통한 빠른 HMR"
  ],
  "installation_steps": [
    "패키지 설치: npm install",
    "환경 변수 설정: .env.local 파일 생성"
  ],
  "run_command": "npm run dev",
  "run_description": "개발 서버가 http://localhost:5173 에서 실행됩니다. 코드 변경 시 자동으로 새로고침됩니다.",
  "usage_examples": [
    "프로덕션 빌드: npm run build",
    "빌드 미리보기: npm run preview"
  ]
}}

**중요:** 프로젝트 타입이 'cli_tool'이고 CLI 명령어가 제공된 경우, run_command는 반드시 그 CLI 명령어를 사용해야 합니다!

이제 주어진 프로젝트 정보를 바탕으로 JSON을 생성해주세요.
**중요: 마크다운 코드블록(```json) 없이 순수 JSON만 출력하세요.**
"""
    
    try:
        response = model.generate_content(context)
        result_text = response.text.strip()
        
        # JSON 코드블록 제거 (있다면)
        if result_text.startswith('```json'):
            result_text = result_text.replace('```json', '').replace('```', '').strip()
        elif result_text.startswith('```'):
            result_text = result_text.replace('```', '').strip()
        
        # JSON 파싱
        ai_content = json.loads(result_text)
        
        # 기본값 설정 (혹시 모를 누락 대비)
        defaults = {
            'description': f"{project_info['languages'][0]} 기반 프로젝트",
            'features': ['프로젝트 기능'],
            'installation_steps': ['패키지 설치'],
            'run_command': 'python main.py',
            'run_description': '프로젝트를 실행합니다.',
            'usage_examples': []
        }
        
        # 누락된 키가 있으면 기본값 사용
        for key, default_value in defaults.items():
            if key not in ai_content:
                ai_content[key] = default_value
        
        return ai_content
        
    except json.JSONDecodeError as e:
        raise Exception(f"AI 응답을 JSON으로 파싱 실패: {e}\n응답: {result_text[:200]}")
    except Exception as e:
        raise Exception(f"AI README 생성 실패: {e}")


# 하위 호환성을 위한 레거시 함수
def generate_description_with_ai(project_info):
    """
    레거시 지원: description만 반환
    """
    try:
        ai_content = generate_readme_with_ai(project_info)
        return ai_content['description']
    except:
        return f"{project_info['languages'][0]} 기반 프로젝트"