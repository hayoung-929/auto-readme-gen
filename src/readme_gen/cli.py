"""CLI 진입점"""
import click
import os
from pathlib import Path
from .analyzer import analyze_project
from .generator import generate_readme


@click.group()
def cli():
    """Auto README Generator - 프로젝트를 분석해서 README를 자동 생성합니다."""
    pass


@cli.command()
@click.argument('project_path', default='.')
def analyze(project_path):
    """
    프로젝트 분석만 수행 (README 생성 안 함)
    
    사용법: readme-gen analyze [프로젝트 경로]
    """
    click.echo(f"프로젝트 분석 중: {project_path}")
    
    project_info = analyze_project(project_path)
    
    click.echo("\n" + "=" * 50)
    click.echo("분석 결과:")
    click.echo("=" * 50)
    click.echo(f"프로젝트 이름: {project_info['name']}")
    click.echo(f"주 언어: {project_info['languages'][0] if project_info['languages'] else 'Unknown'}")
    click.echo(f"총 파일 수: {project_info['file_count']}")
    click.echo(f"Docker 지원: {'예' if project_info['has_docker'] else '아니오'}")
    click.echo(f"requirements.txt: {'있음' if project_info['has_requirements'] else '없음'}")
    
    # Git 정보 표시
    if project_info['git']['has_git']:
        click.echo("\nGit 정보:")
        if 'username' in project_info['git']:
            click.echo(f"  GitHub 사용자: {project_info['git']['username']}")
            click.echo(f"  저장소 이름: {project_info['git']['repo_name']}")
            click.echo(f"  Clone URL: {project_info['git']['clone_url']}")


@cli.command()
@click.argument('project_path', default='.')
@click.option('--output', '-o', default='README.md', help='출력 파일명 (기본: README.md)')
@click.option('--lang', '-l', type=click.Choice(['korean', 'english']), default='korean', help='템플릿 언어 (기본: korean)')
@click.option('--template', '-t', default=None, help='사용할 템플릿 파일 경로')
@click.option('--description', '-d', default=None, help='프로젝트 설명 (입력 안 하면 대화형으로 물어봄)')
@click.option('--no-interactive', is_flag=True, help='대화형 입력 건너뛰기 (기본값 사용)')
def generate(project_path, output, lang, template, description, no_interactive):
    """
    프로젝트를 분석해서 README 생성
    
    사용법: 
      readme-gen generate .                    # 대화형
      readme-gen generate . -d "설명"          # 설명 직접 입력
      readme-gen generate . --no-interactive   # 기본값 사용
    """
    
    try:
        click.echo(f"프로젝트 분석 중: {project_path}")
        
        # 1. 프로젝트 분석
        project_info = analyze_project(project_path)
        
        # 빈 프로젝트 체크
        if project_info.get('is_empty', False):
            click.echo("⚠️  경고: 프로젝트 폴더가 비어있습니다.")
            if not click.confirm('그래도 README를 생성하시겠습니까?'):
                click.echo("취소되었습니다.")
                return
        
        click.echo(f"✓ 감지된 프로젝트: {project_info['name']}")
        
        # 주 언어 감지
        main_lang = project_info['languages'][0] if project_info['languages'] else 'software'
        
        # 2. 프로젝트 설명 입력받기
        if description is None and not no_interactive:
            click.echo("\n" + "=" * 50)
            click.echo("프로젝트 정보 입력")
            click.echo("=" * 50)
            
            # 기본 설명 제안
            default_desc = f"A {main_lang} project"
            if lang == 'korean':
                default_desc = f"{main_lang} 기반 프로젝트"
            
            description = click.prompt(
                '프로젝트 설명을 입력하세요 (엔터: 기본값 사용)',
                default=default_desc,
                show_default=True
            )
            
            click.echo(f"\n✓ 설명: {description}")
        
        elif description is None:
            # --no-interactive 옵션이거나 -d로 설명 안 줬을 때
            if lang == 'korean':
                description = f"{main_lang} 기반 프로젝트"
            else:
                description = f"A {main_lang} project"
        
        # 프로젝트 정보에 설명 추가
        project_info['description'] = description
        
        # 3. 템플릿 경로 설정
        if template is None:
            script_dir = Path(__file__).parent.parent.parent
            template = script_dir / 'templates' / f'{lang}.md'
        
        # 템플릿 파일 존재 확인
        if not Path(template).exists():
            click.echo(f"❌ 에러: 템플릿 파일을 찾을 수 없습니다: {template}")
            click.echo(f"사용 가능한 템플릿: korean.md, english.md")
            return
        
        # 4. 출력 경로 설정
        project_root = Path(project_path).resolve()
        output_path = project_root / output
        
        # 5. README 생성
        click.echo(f"\nREADME 생성 중... (언어: {lang})")
        generate_readme(project_info, str(template), str(output_path))
        
        click.echo(f"✓ 완료! 생성된 파일: {output_path}")
        
    except ValueError as e:
        click.echo(f"❌ 에러: {e}")
        return
    except FileNotFoundError as e:
        click.echo(f"❌ 파일을 찾을 수 없습니다: {e}")
        return
    except Exception as e:
        click.echo(f"❌ 예상치 못한 에러가 발생했습니다: {e}")
        click.echo("문제가 계속되면 GitHub Issues에 제보해주세요.")
        return


if __name__ == '__main__':
    cli()