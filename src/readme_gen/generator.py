"""README 생성 모듈"""
from pathlib import Path
from jinja2 import Template

def generate_readme(project_info, template_path='templates/default.md', output_path='README_generated.md'):
    """
    프로젝트 정보를 받아서 README 파일 생성
    
    Args:
        project_info: analyzer.py에서 추출한 프로젝트 정보 (dict)
        template_path: 템플릿 파일 경로
        output_path: 생성될 README 파일 경로
    """
    

    with open(template_path, 'r', encoding='utf-8') as f:
        template_content = f.read()
    
    template = Template(template_content)
    
    data = {
        'name': project_info.get('name', 'Unknown Project'),
        'description': project_info.get('description', 'A Python project'),
        'main_language': project_info['languages'][0] if project_info['languages'] else 'Unknown',
        'languages': project_info['languages'],
        'file_count': project_info['file_count'],
        'has_requirements': project_info['has_requirements'],
        'has_package_json': project_info['has_package_json'],
        'has_docker': project_info['has_docker'],
        'extensions': project_info['extensions'],
        'git': project_info.get('git', {'has_git': False}),
    }
    
    rendered_content = template.render(**data)
    
    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(rendered_content)
    
    print(f"README 파일 생성 완료: {output_path}")
    return output_path

if __name__ == '__main__':
    import sys
    import os
    
    sys.path.insert(0, os.path.dirname(__file__))
    from analyzer import analyze_project
    
    print("프로젝트 분석 중...")
    project_root = os.path.join(os.path.dirname(__file__), '../..')
    project_info = analyze_project(project_root)
    
    print(f"감지된 프로젝트 이름: {project_info['name']}")

    print("\nREADME 생성 중...")
    template_path = os.path.join(project_root, 'templates/default.md')
    output_path = os.path.join(project_root, 'README_generated.md')
    output = generate_readme(project_info, template_path, output_path)
    
    print(f"\n생성된 파일을 확인하세요: {output}")