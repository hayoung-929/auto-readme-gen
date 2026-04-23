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
pip install git+https://github.com/hayoung-929/auto-readme-gen.git
```

### 3초만에 README 만들기

```bash
cd your-project
readme-gen generate .
```

끝! 프로젝트 폴더에 `README.md` 파일이 생성됩니다.

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

### 2. 한 줄로 끝내기

프로젝트 설명을 직접 입력:

```bash
readme-gen generate . -d "Django 블로그 웹사이트"
```

영어 버전으로 생성:

```bash
readme-gen generate . --lang english -d "Django blog website"
```

---

### 3. 고급 옵션

#### 출력 파일명 변경

```bash
# README_KR.md로 저장
readme-gen generate . -o README_KR.md

# 영어 버전도 따로 생성
readme-gen generate . --lang english -o README_EN.md
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

### 예시 1: 새 프로젝트 시작

```bash
# 1. 프로젝트 폴더 생성
mkdir my-awesome-app
cd my-awesome-app

# 2. Git 초기화
git init
git remote add origin https://github.com/username/my-awesome-app.git

# 3. 코드 작성...
echo "print('Hello')" > main.py

# 4. README 생성
readme-gen generate . -d "내 멋진 Python 앱"

# 5. 완성!
git add .
git commit -m "Initial commit with README"
git push origin main
```

### 예시 2: 기존 프로젝트에 README 추가

```bash
# 프로젝트 폴더로 이동
cd ~/projects/old-project

# README 생성 (대화형)
readme-gen generate .
> 프로젝트 설명: 2020년에 만든 Flask 웹앱

# Git에 추가
git add README.md
git commit -m "docs: Add README"
git push
```

### 예시 3: 다국어 README

```bash
# 한글 버전
readme-gen generate . --lang korean -o README_KR.md

# 영어 버전
readme-gen generate . --lang english -o README_EN.md

# 둘 다 커밋
git add README_*.md
git commit -m "docs: Add multilingual README"
```

---

## 🔧 개발자 가이드

### 소스에서 설치

```bash
# 1. 저장소 클론
git clone https://github.com/hayoung-929/auto-readme-gen.git
cd auto-readme-gen

# 2. 가상환경 생성
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate

# 3. 개발 모드로 설치
pip install -e .
```

### 커스텀 템플릿 만들기

`templates/` 폴더에 있는 `korean.md` 또는 `english.md`를 참고하여 나만의 템플릿을 만들 수 있습니다.

**템플릿 변수:**
- `{{ name }}` - 프로젝트 이름
- `{{ description }}` - 프로젝트 설명
- `{{ main_language }}` - 주 언어
- `{{ languages }}` - 사용 언어 목록
- `{{ git.username }}` - GitHub 사용자명
- `{{ git.clone_url }}` - Clone URL
- `{{ has_docker }}` - Docker 사용 여부
- `{{ file_count }}` - 총 파일 수

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

**Q: 다른 프로그래밍 언어도 지원하나요?**  
A: Python, JavaScript, TypeScript, Go, Rust, Java, C++, C, Ruby, PHP를 지원합니다.

**Q: 템플릿을 수정할 수 있나요?**  
A: 네! `templates/` 폴더의 파일을 수정하거나, `--template` 옵션으로 커스텀 템플릿을 사용할 수 있습니다.

**Q: GitHub 없는 프로젝트도 가능한가요?**  
A: 가능합니다. Git 정보가 없으면 해당 섹션이 자동으로 제외됩니다.

**Q: 기존 README를 덮어쓰나요?**  
A: 기본적으로 `README.md`로 생성되므로 주의하세요. `-o` 옵션으로 다른 파일명을 사용하거나, 백업 후 사용하세요.

---

## 📬 문의

- GitHub Issues: [https://github.com/hayoung-929/auto-readme-gen/issues](https://github.com/hayoung-929/auto-readme-gen/issues)
- Email: s26017@gsm.hs.kr

---

<div align="center">

**Made with ❤️ by [hayoung-929](https://github.com/hayoung-929)**

⭐ 이 프로젝트가 도움이 되었다면 Star를 눌러주세요!

</div>