# {{ name }}

<div align="center">

{% if git.has_git and git.username and git.repo_name %}
![GitHub stars](https://img.shields.io/github/stars/{{ git.username }}/{{ git.repo_name }}?style=social)
![GitHub forks](https://img.shields.io/github/forks/{{ git.username }}/{{ git.repo_name }}?style=social)
{% endif %}

{% if main_language %}
![{{ main_language }}](https://img.shields.io/badge/{{ main_language }}-3776AB?style=for-the-badge&logo=python&logoColor=white)
{% endif %}

{% if has_docker %}
![Docker](https://img.shields.io/badge/Docker-2496ED?style=for-the-badge&logo=docker&logoColor=white)
{% endif %}

![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

</div>

{{ description }}

---

## 프로젝트 소개

이 프로젝트는 **{{ main_language }}**로 개발되었습니다.

---

## 시작하기

{% if has_requirements %}
### 설치 방법

**1. 저장소 복제**
```bash
{% if git.has_git and git.clone_url %}
git clone {{ git.clone_url }}
{% else %}
git clone https://github.com/YOUR_USERNAME/{{ name }}.git
{% endif %}
cd {{ name }}
```

**2. 가상환경 설정**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

**3. 패키지 설치**
```bash
pip install -r requirements.txt
```
{% endif %}

{% if has_package_json %}
### 설치 방법

```bash
npm install
npm start
```
{% endif %}

---

## 기술 스택

{% for lang in languages %}
- {{ lang }}
{% endfor %}

{% if has_docker %}
---

## Docker 사용법

```bash
docker build -t {{ name }} .
docker run -p 8000:8000 {{ name }}
```
{% endif %}

---

## 프로젝트 정보

| 항목 | 내용 |
|------|------|
| 총 파일 수 | {{ file_count }}개 |
| 주 언어 | {{ main_language }} |
{% if git.has_git and git.remote_url %}
| 저장소 | [{{ git.username }}/{{ git.repo_name }}]({{ git.remote_url }}) |
{% endif %}

---

## 파일 구성

{% for ext, count in extensions.items() %}
- **{{ ext }}** : {{ count }}개
{% endfor %}

---

<div align="center">

*이 README는 [auto-readme-gen](https://github.com/hayoung-929/auto-readme-gen)으로 자동 생성되었습니다.*

</div>