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
    
    # 템플릿 파일 읽기 (에러 처리 추가)
    try:
        with open(template_path, 'r', encoding='utf-8') as f:
            template_content = f.read()
    except FileNotFoundError:
        raise FileNotFoundError(f"템플릿 파일을 찾을 수 없습니다: {template_path}")
    except Exception as e:
        raise Exception(f"템플릿 파일 읽기 실패: {e}")
    
    try:
        # Jinja2 템플릿 객체 생성
        template = Template(template_content)
        
        # 템플릿에 넣을 데이터 준비
        data = {
            'name': project_info.get('name', 'Unknown Project'),
            'description': project_info.get('description', 'A project'),
            'main_language': project_info['languages'][0] if project_info['languages'] else 'Unknown',
            'languages': project_info['languages'],
            'file_count': project_info['file_count'],
            'has_requirements': project_info['has_requirements'],
            'has_package_json': project_info['has_package_json'],
            'has_docker': project_info['has_docker'],
            'extensions': project_info['extensions'],
            'git': project_info.get('git', {'has_git': False}),
        }
        
        # 템플릿에 데이터 채워넣기 (렌더링)
        rendered_content = template.render(**data)
        
        # 파일로 저장
        with open(output_path, 'w', encoding='utf-8') as f:
            f.write(rendered_content)
        
        print(f"README 파일 생성 완료: {output_path}")
        return output_path
        
    except Exception as e:
        raise Exception(f"README 생성 중 에러 발생: {e}")