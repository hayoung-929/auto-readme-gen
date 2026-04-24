# auto-readme-gen

<div align="center">

![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

**프로젝트를 분석해서 README.md를 자동으로 생성하는 CLI 도구**

Git 정보, 사용 언어, 파일 구조 등을 자동으로 파악하여 전문적인 README를 몇 초 만에 만들어줍니다.

[설치하기](#설치) · [사용법](#사용법) · [기능](#주요-기능)

</div>

---

## 📌 주요 기능

- 🔍 **자동 프로젝트 분석** - 언어, 프레임워크, 파일 구조 자동 감지
- 🤖 **AI 기반 설명 생성** - Gemini AI로 프로젝트 설명, 주요 기능, 실행 방법 자동 생성
- 🔗 **Git 정보 추출** - GitHub 저장소 URL, 사용자명 자동 인식
- 🌐 **다국어 지원** - 한글/영어 템플릿 제공
- 🎨 **GitHub 뱃지** - Stars, Language, License 뱃지 자동 생성
- 💬 **대화형 입력** - 프로젝트 설명을 쉽게 입력
- ⚙️ **커스터마이징** - 템플릿 수정 및 확장 가능
- 🛡️ **안정성** - 경로 검증, 에러 처리 완비

---

## 🚀 빠른 시작

### 설치

```bash
# 저장소 복제
git clone https://github.com/hayoung-929/auto-readme-gen.git
cd auto-readme-gen

# 가상환경 설정
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 패키지 설치
pip install -r requirements.txt

# 개발 모드 설치
pip install -e .
```

### 3초만에 README 만들기

```bash
cd your-project
readme-gen generate .
```

끝! 프로젝트 폴더에 `README.md` 파일이 생성됩니다.

---

## 🤖 AI 기능 사용하기

### 1. Gemini API 키 발급

1. https://ai.google.dev 접속
2. Google 계정으로 로그인
3. **Get API key** 클릭
4. **Create API key in new project** 선택
5. API 키 복사

### 2. 환경변수 설정

**일회성 (터미널 닫으면 사라짐):**
```bash
export GEMINI_API_KEY='your-api-key-here'
```

**영구 설정 (추천):**
```bash
# .bashrc 파일 열기
nano ~/.bashrc

# 맨 아래 추가
export GEMINI_API_KEY='your-api-key-here'

# 저장 (Ctrl+X, Y, Enter)

# 적용
source ~/.bashrc
```

### 3. AI로 README 생성

```bash
# AI가 모든 내용 자동 생성!
readme-gen generate . --ai
```

**AI가 생성하는 내용:**
- ✨ 프로젝트 설명 (2-3문장)
- 📋 주요 기능 목록 (4-6개)
- 📦 설치 방법 (프레임워크별)
- ▶️ 실행 명령어 (정확한 커맨드)
- 💡 사용 예시

### 무료 사용량

- **하루 1,500번** 무료
- 개인 프로젝트는 **평생 무료**로 충분
- 유료 전환해도 매우 저렴 (1만번에 ~1,300원)

---

## 📖 상세 사용법

### 1. 기본 사용 (대화형)

```bash
cd my-project
readme-gen generate .
```

**실행 화면:**
프로젝트 분석 중: .
✓ 감지된 프로젝트: my-project
==================================================
프로젝트 정보 입력
프로젝트 설명을 입력하세요: Flask 기반 REST API 서버
✓ 설명: Flask 기반 REST API 서버
README 생성 중... (언어: korean)
✓ 완료! 생성된 파일: /path/to/my-project/README.md

---

### 2. AI 자동 생성 (추천!)

```bash
# AI가 전부 알아서!
readme-gen generate . --ai
```

**실행 화면:**
프로젝트 분석 중: .
✓ 감지된 프로젝트: my-project
🤖 AI가 프로젝트를 분석하고 README를 생성하고 있습니다...
(분석 중: 설명, 주요 기능, 설치 방법, 실행 방법...)
✓ AI 생성 완료!
설명: Flask와 SQLAlchemy를 사용하는 REST API 서버입니다...
주요 기능: 5개
실행 명령어: flask run
README 생성 중... (언어: korean)
✓ 완료! 생성된 파일: /path/to/my-project/README.md

---

### 3. 고급 옵션

#### 영어 버전으로 생성

```bash
readme-gen generate . --lang english --ai
```

#### 출력 파일명 변경

```bash
# README_KR.md로 저장
readme-gen generate . -o README_KR.md --ai

# 영어 버전도 따로 생성
readme-gen generate . --lang english -o README_EN.md --ai
```

#### 설명 직접 입력 (AI 없이)

```bash
readme-gen generate . -d "Django 블로그 웹사이트"
```

#### 대화형 입력 건너뛰기

```bash
# 기본값으로 바로 생성
readme-gen generate . --no-interactive
```

#### 커스텀 템플릿 사용

```bash
readme-gen generate . --template ./my-template.md
```

#### 프로젝트 분석만 (README 생성 안 함)

```bash
readme-gen analyze .
```

**출력 예시:**
==================================================
분석 결과:
프로젝트 이름: my-project
주 언어: Python
총 파일 수: 25
Docker 지원: 예
requirements.txt: 있음
Git 정보:
GitHub 사용자: hayoung-929
저장소 이름: my-project
Clone URL: https://github.com/hayoung-929/my-project.git

---

## 🎯 실제 사용 예시

### 예시 1: Flask API 프로젝트

```bash
cd flask-api-project
readme-gen generate . --ai
```

**AI가 자동 감지:**
- ✅ Flask 프레임워크 인식
- ✅ `flask run` 명령어 생성
- ✅ requirements.txt 분석
- ✅ Docker 설정 확인
- ✅ 포트 정보 추출

---

### 예시 2: React 프론트엔드

```bash
cd react-dashboard
readme-gen generate . --lang english --ai
```

**AI가 자동 감지:**
- ✅ React + TypeScript 인식
- ✅ `npm run dev` 명령어 생성
- ✅ package.json scripts 분석
- ✅ Vite/CRA 빌드 도구 확인

---

### 예시 3: CLI 도구

```bash
cd my-cli-tool
readme-gen generate . --ai
```

**AI가 자동 감지:**
- ✅ setup.py에서 CLI 명령어 추출
- ✅ `my-cli [command]` 형식 생성
- ✅ 서브커맨드 예시 생성

---

## 🔧 개발자 가이드

### 지원하는 프로젝트 타입

- **Python:** Flask, Django, FastAPI, CLI 도구, 일반 스크립트
- **JavaScript/TypeScript:** React, Vue.js, Next.js, Express.js, Node.js
- **기타:** Go, Rust, Java, C++, C, Ruby, PHP

### 감지하는 정보

- 📦 프레임워크 (Flask, Django, React 등)
- 🔧 주요 패키지 (requirements.txt, package.json)
- 📝 엔트리 포인트 (main.py, app.py, index.js)
- ⚙️ CLI 명령어 (setup.py의 console_scripts)
- 🐳 Docker 설정 (Dockerfile, 포트)
- 📂 프로젝트 구조
- 🔗 Git 저장소 정보

### 커스텀 템플릿 만들기

`templates/` 폴더의 `korean.md` 또는 `english.md`를 참고하여 나만의 템플릿을 만들 수 있습니다.

**템플릿 변수:**
```jinja2
{{ name }}                    # 프로젝트 이름
{{ description }}             # 프로젝트 설명
{{ main_language }}           # 주 언어
{{ ai_features }}             # AI 생성 주요 기능 (리스트)
{{ ai_run_command }}          # AI 생성 실행 명령어
{{ ai_installation }}         # AI 생성 설치 단계 (리스트)
{{ git.username }}            # GitHub 사용자명
{{ git.clone_url }}           # Clone URL
{{ has_docker }}              # Docker 사용 여부
```

---

## 🤝 기여하기

버그 제보, 기능 제안, PR 모두 환영합니다!

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 라이선스

MIT License - 자유롭게 사용하세요!

---

## 🙋‍♂️ FAQ

**Q: AI 없이도 사용 가능한가요?**  
A: 네! `--ai` 옵션 없이 실행하면 대화형으로 설명을 입력받거나 기본 템플릿으로 생성됩니다.

**Q: API 키 없으면 어떻게 되나요?**  
A: `--ai` 옵션 사용 시에만 API 키가 필요합니다. 없이 실행하면 수동 입력 모드로 전환됩니다.

**Q: 어떤 프로그래밍 언어를 지원하나요?**  
A: Python, JavaScript, TypeScript, Go, Rust, Java, C++, C, Ruby, PHP를 지원합니다.

**Q: 템플릿을 수정할 수 있나요?**  
A: 네! `templates/` 폴더의 파일을 수정하거나, `--template` 옵션으로 커스텀 템플릿을 사용할 수 있습니다.

**Q: GitHub 없는 프로젝트도 가능한가요?**  
A: 가능합니다. Git 정보가 없으면 해당 섹션이 자동으로 제외됩니다.

**Q: 기존 README를 덮어쓰나요?**  
A: 기본적으로 `README.md`로 생성되므로 주의하세요. `-o` 옵션으로 다른 파일명을 사용하거나, 백업 후 사용하세요.

**Q: AI가 잘못된 정보를 생성하면?**  
A: `-d` 옵션으로 설명을 직접 입력하거나, 생성된 README를 수동으로 수정하세요.

---

## 📬 문의

- GitHub: [@hayoung-929](https://github.com/hayoung-929)
- Issues: [auto-readme-gen/issues](https://github.com/hayoung-929/auto-readme-gen/issues)
- Email: s26017@gsm.hs.kr

---

<div align="center">

**Made with ❤️ by [hayoung-929](https://github.com/hayoung-929)**

⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!

</div>