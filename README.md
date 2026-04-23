# auto-readme-gen

<div align="center">


![GitHub stars](https://img.shields.io/github/stars/hayoung-929/auto-readme-gen?style=social)
![GitHub forks](https://img.shields.io/github/forks/hayoung-929/auto-readme-gen?style=social)



![Python](https://img.shields.io/badge/Python-3776AB?style=for-the-badge&logo=python&logoColor=white)




![License](https://img.shields.io/badge/License-MIT-yellow.svg?style=for-the-badge)

</div>

프로젝트를 분석해서 README.md를 자동으로 생성하는 CLI 도구입니다.
Git 정보, 사용 언어, 파일 구조 등을 자동으로 파악하여 전문적인 README를 몇 초 만에 만들어줍니다.

---

## 프로젝트 소개

이 프로젝트는 **Python**로 개발되었습니다.

---

## 시작하기


### 설치 방법

**1. 저장소 복제**
```bash

git clone https://github.com/hayoung-929/auto-readme-gen.git

cd auto-readme-gen
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




---

## 기술 스택


- Python

---

## 주요 기능

- 🔍 프로젝트 자동 분석 (언어, 프레임워크, 파일 구조)
- 🔗 Git/GitHub 정보 자동 추출 (저장소 URL, 사용자명)
- 🌐 한글/영어 템플릿 지원
- 🎨 GitHub 뱃지 자동 생성
- 💬 대화형 프로젝트 설명 입력
- ⚙️ 커스터마이징 가능한 템플릿

---

## 설치

### 방법 1: pip로 설치 (추천)

```bash
pip install git+https://github.com/hayoung-929/auto-readme-gen.git
```

### 방법 2: 소스에서 설치

```bash
git clone https://github.com/hayoung-929/auto-readme-gen.git
cd auto-readme-gen
pip install -e .
```

---

## 사용법

### 기본 사용

```bash
cd your-project
readme-gen generate .
```

대화형으로 프로젝트 설명을 입력하면 README.md가 자동 생성됩니다.

### 고급 옵션

```bash
readme-gen generate . --lang english
readme-gen generate . --lang korean

readme-gen generate . -d "내 프로젝트 설명"

readme-gen generate . -o README_KR.md

readme-gen generate . --no-interactive

readme-gen analyze .
```

### 사용 예시

```bash
cd ~/projects/my-awesome-project

readme-gen generate .

프로젝트 설명을 입력하세요: Flask 기반 REST API 서버

✓ 완료! 생성된 파일: ~/projects/my-awesome-project/README.md
```

---

## 기여하기

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 라이선스

MIT License - 자유롭게 사용하세요!


---

## 프로젝트 정보

| 항목 | 내용 |
|------|------|
| 총 파일 수 | 16개 |
| 주 언어 | Python |

| 저장소 | [hayoung-929/auto-readme-gen](https://github.com/hayoung-929/auto-readme-gen) |


---

## 파일 구성


- **.md** : 3개

- **.txt** : 6개

- **.py** : 5개


---

<div align="center">

*이 README는 [auto-readme-gen](https://github.com/hayoung-929/auto-readme-gen)으로 자동 생성되었습니다.*

</div>