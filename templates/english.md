templates/english.md 전체 (개선 버전)
위치: templates/english.md
markdown# {{ name }}

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

## 📌 Key Features

{% if main_language == 'Python' %}
- 🐍 Python-based application
{% if has_requirements %}
- 📦 Dependency management (requirements.txt)
{% endif %}
{% endif %}

{% if has_docker %}
- 🐳 Docker containerization support
{% endif %}

{% if git.has_git %}
- 🔗 Git version control
{% endif %}

- ⚡ Built with {{ languages|join(', ') }}
- 📁 {{ file_count }} files in total

---

## 🚀 Quick Start

### Installation

{% if git.has_git and git.clone_url %}
**Clone the repository**
```bash
git clone {{ git.clone_url }}
cd {{ name }}
```
{% endif %}

{% if main_language == 'Python' %}
**Set up virtual environment (recommended)**
```bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
```

{% if has_requirements %}
**Install dependencies**
```bash
pip install -r requirements.txt
```
{% endif %}
{% endif %}

{% if has_package_json %}
**Install packages**
```bash
npm install
# or
yarn install
```
{% endif %}

---

## 📖 Usage

### Basic Execution

{% if main_language == 'Python' %}
```bash
# Run Python script
python main.py
```
{% elif main_language == 'JavaScript' or main_language == 'TypeScript' %}
```bash
# Start development server
npm run dev

# Production build
npm run build

# Start server
npm start
```
{% endif %}

{% if has_docker %}
### Running with Docker

```bash
# Build image
docker build -t {{ name }} .

# Run container
docker run -p 8000:8000 {{ name }}
```

**Using Docker Compose**
```bash
docker-compose up -d
```
{% endif %}

---

## 🛠️ Development

### Prerequisites

{% if main_language == 'Python' %}
- Python 3.7 or higher
{% elif main_language == 'JavaScript' or main_language == 'TypeScript' %}
- Node.js 14 or higher
- npm or yarn
{% elif main_language == 'Go' %}
- Go 1.16 or higher
{% elif main_language == 'Rust' %}
- Rust 1.50 or higher
- Cargo
{% elif main_language == 'Java' %}
- JDK 11 or higher
- Maven or Gradle
{% endif %}

{% if has_docker %}
- Docker (optional)
{% endif %}

### Tech Stack

{% for lang in languages %}
- {{ lang }}
{% endfor %}

---

## 📁 Project Structure
{{ name }}/
{% if has_docker %}
├── Dockerfile
{% if has_package_json or has_requirements %}
├── docker-compose.yml
{% endif %}
{% endif %}
{% if has_requirements %}
├── requirements.txt
{% endif %}
{% if has_package_json %}
├── package.json
{% endif %}
├── README.md
{% if main_language == 'Python' %}
├── main.py
└── src/
{% elif main_language == 'JavaScript' or main_language == 'TypeScript' %}
├── index.js
└── src/
{% endif %}

---

## 🔧 Configuration

{% if main_language == 'Python' %}
### Environment Variables

Create a `.env` file in the project root:

```env
# Example
DEBUG=True
SECRET_KEY=your-secret-key
DATABASE_URL=sqlite:///db.sqlite3
```
{% endif %}

{% if has_package_json %}
### Environment Variables

Create a `.env.local` file:

```env
REACT_APP_API_URL=http://localhost:3000
REACT_APP_ENV=development
```
{% endif %}

---

## 🤝 Contributing

Contributions are welcome! Please follow these steps:

1. Fork the Project
2. Create your Feature Branch (`git checkout -b feature/AmazingFeature`)
3. Commit your Changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the Branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

---

## 📝 License

MIT License - Feel free to use this project!

---

## 📬 Contact

{% if git.has_git and git.username %}
- GitHub: [@{{ git.username }}](https://github.com/{{ git.username }})
{% if git.repo_name %}
- Issues: [{{ git.repo_name }}/issues](https://github.com/{{ git.username }}/{{ git.repo_name }}/issues)
{% endif %}
{% endif %}

---

## 🙏 Acknowledgments

{% if git.has_git and git.username and git.repo_name %}
If this project helped you, please give it a ⭐️ Star!

[![GitHub stars](https://img.shields.io/github/stars/{{ git.username }}/{{ git.repo_name }}?style=social)](https://github.com/{{ git.username }}/{{ git.repo_name }})
{% endif %}

---

<div align="center">

*This README was automatically generated with [auto-readme-gen](https://github.com/hayoung-929/auto-readme-gen).*

</div>