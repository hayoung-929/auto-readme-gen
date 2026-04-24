# auto-readme-gen

<div align="center">


![GitHub stars](https://img.shields.io/github/stars/hayoung-929/auto-readme-gen?style=social)
![GitHub forks](https://img.shields.io/github/forks/hayoung-929/auto-readme-gen?style=social)



![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)


![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

</div>

Python으로 개발된 CLI 도구입니다. Click 프레임워크를 기반으로 하며, `gitpython`과 `pygithub`를 이용해 프로젝트의 Git 정보 및 기술 스택을 분석합니다. `jinja2` 템플릿과 `google-generativeai`를 활용하여 전문적인 README 파일을 자동으로 생성합니다.

---

## 📌 주요 기능



- 프로젝트 Git 정보 및 기술 스택 자동 분석

- Jinja2 템플릿 기반의 README 파일 생성

- Google Generative AI를 활용한 README 설명 자동 생성

- Click 프레임워크를 이용한 직관적인 CLI 인터페이스

- Python `requirements.txt` 기반 종속성 관리



---

## 🚀 빠른 시작

### 설치


**저장소 복제**
```bash
git clone https://github.com/hayoung-929/auto-readme-gen.git
cd auto-readme-gen
```




**1. 저장소 복제**
```bash
`git clone https
```

**2. 가상환경 생성**
```bash
`python -m venv venv`
```

**3. 가상환경 활성화**
```bash
`source venv/bin/activate` (Windows
```

**4. 개발 모드 설치**
```bash
`pip install -e .`
```



---

## 📖 사용법

### 실행


```bash
readme-gen generate .
```

현재 디렉토리의 프로젝트를 분석하여 `README.md` 파일을 생성합니다. `--ai` 옵션을 추가하여 AI 기반 설명을 README에 포함할 수 있습니다.



### 사용 예시


```bash
프로젝트 분석만 수행: `readme-gen analyze .`
```

```bash
AI 기반 README 생성: `readme-gen generate . --ai`
```

```bash
영문 README 생성: `readme-gen generate . --lang english`
```





---

## 🛠️ 개발 환경

### 필수 요구사항


- Python 3.7 이상




### 기술 스택


- Python


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


- GitHub: [@hayoung-929](https://github.com/hayoung-929)

- Issues: [auto-readme-gen/issues](https://github.com/hayoung-929/auto-readme-gen/issues)



---

## 🙏 감사합니다


이 프로젝트가 도움이 되었다면 ⭐️ Star를 눌러주세요!

[![GitHub stars](https://img.shields.io/github/stars/hayoung-929/auto-readme-gen?style=social)](https://github.com/hayoung-929/auto-readme-gen)


---

<div align="center">

*이 README는 [auto-readme-gen](https://github.com/hayoung-929/auto-readme-gen)으로 자동 생성되었습니다.*

</div>