# {{ name }}

<div align="center">

{% if git.has_git and git.username %}
![GitHub stars](https://img.shields.io/github/stars/{{ git.username }}/{{ git.repo_name }}?style=social)
![GitHub forks](https://img.shields.io/github/forks/{{ git.username }}/{{ git.repo_name }}?style=social)
{% endif %}

{% if main_language == 'Python' %}
![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)
{% elif main_language == 'JavaScript' %}
![JavaScript](https://img.shields.io/badge/JavaScript-F7DF1E?style=for-the-badge&logo=javascript&logoColor=black)
{% elif main_language == 'TypeScript' %}
![TypeScript](https://img.shields.io/badge/TypeScript-3178C6?style=for-the-badge&logo=typescript&logoColor=white)
{% elif main_language == 'Go' %}
![Go](https://img.shields.io/badge/Go-00ADD8?style=for-the-badge&logo=go&logoColor=white)
{% elif main_language == 'Rust' %}
![Rust](https://img.shields.io/badge/Rust-000000?style=for-the-badge&logo=rust&logoColor=white)
{% elif main_language == 'Java' %}
![Java](https://img.shields.io/badge/Java-ED8B00?style=for-the-badge&logo=openjdk&logoColor=white)
{% endif %}

![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

</div>

{{ description }}

---

## 📌 주요 기능

{% if ai_features %}
{% for feature in ai_features %}
- {{ feature }}
{% endfor %}
{% else %}
{% if main_language == 'Python' %}
- 🐍 Python 기반 애플리케이션
{% if has_requirements %}
- 📦 의존성 관리 (requirements.txt)
{% endif %}
{% endif %}

{% if has_docker %}
- 🐳 Docker 컨테이너화 지원
{% endif %}

{% if git.has_git %}
- 🔗 Git 버전 관리
{% endif %}

- ⚡ {{ languages|join(', ') }} 활용
- 📁 총 {{ file_count }}개 파일로 구성
{% endif %}

---

## 🚀 빠른 시작

### 설치

{% if git.has_git and git.clone_url %}
**저장소 복제**
```bash
git clone {{ git.clone_url }}
cd {{ name }}
```
{% endif %}

{% if ai_installation %}
{% for step in ai_installation %}
**{{ loop.index }}. {{ step.split(':')[0] if ':' in step else '설치' }}**
```bash
{{ step.split(':')[1].strip() if ':' in step else step }}
```
{% endfor %}
{% else %}
{% if main_language == 'Python' %}
**가상환경 설정 (권장)**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

{% if has_requirements %}
**의존성 설치**
```bash
pip install -r requirements.txt
```
{% endif %}
{% endif %}

{% if has_package_json %}
**패키지 설치**
```bash
npm install
# 또는
yarn install
```
{% endif %}
{% endif %}

---

## 📖 사용법

### 실행

{% if ai_run_command %}
```bash
{{ ai_run_command }}
```

{{ ai_run_description }}
{% else %}
{% if main_language == 'Python' %}
```bash
# Python 스크립트 실행
python main.py
```
{% elif main_language == 'JavaScript' or main_language == 'TypeScript' %}
```bash
# 개발 서버 실행
npm run dev

# 프로덕션 빌드
npm run build

# 서버 시작
npm start
```
{% endif %}
{% endif %}

{% if ai_usage_examples %}
### 사용 예시

{% for example in ai_usage_examples %}
```bash
{{ example }}
```
{% endfor %}
{% endif %}

{% if has_docker %}
### Docker로 실행

```bash
# 이미지 빌드
docker build -t {{ name }} .

# 컨테이너 실행
docker run -p 8000:8000 {{ name }}
```

**Docker Compose 사용**
```bash
docker-compose up -d
```
{% endif %}

---

## 🛠️ 개발 환경

### 필수 요구사항

{% if main_language == 'Python' %}
- Python 3.7 이상
{% elif main_language == 'JavaScript' or main_language == 'TypeScript' %}
- Node.js 14 이상
- npm 또는 yarn
{% elif main_language == 'Go' %}
- Go 1.16 이상
{% elif main_language == 'Rust' %}
- Rust 1.50 이상
- Cargo
{% elif main_language == 'Java' %}
- JDK 11 이상
- Maven 또는 Gradle
{% endif %}

{% if has_docker %}
- Docker (선택사항)
{% endif %}

### 기술 스택

{% for lang in languages %}
- {{ lang }}
{% endfor %}

---

## 🤝 기여하기

기여를 환영합니다! 다음 단계를 따라주세요:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 라이선스

MIT License - 자유롭게 사용하세요!

---

## 📬 문의

{% if git.has_git and git.username %}
- GitHub: [@{{ git.username }}](https://github.com/{{ git.username }})
{% if git.repo_name %}
- Issues: [{{ git.repo_name }}/issues](https://github.com/{{ git.username }}/{{ git.repo_name }}/issues)
{% endif %}
{% endif %}

---

## 🙏 감사합니다

{% if git.has_git and git.username and git.repo_name %}
이 프로젝트가 도움이 되었다면 ⭐️ Star를 눌러주세요!

[![GitHub stars](https://img.shields.io/github/stars/{{ git.username }}/{{ git.repo_name }}?style=social)](https://github.com/{{ git.username }}/{{ git.repo_name }})
{% endif %}

---

<div align="center">

*이 README는 [auto-readme-gen](https://github.com/hayoung-929/auto-readme-gen)으로 자동 생성되었습니다.*

</div>