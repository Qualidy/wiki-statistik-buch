import os
import yaml


def define_env(env):
    @env.macro
    def task(file=None, **parameter):
        params = dict()

        if file:
            file_path = os.path.join(env.project_dir, file)
            with open(file_path, 'r', encoding='utf-8') as file:
                params.update(yaml.safe_load(file))

        params.update(parameter)

        return create_task(**params)

    @env.macro
    def youtube_video(inner_url, title='Video'):
        return youtube_video_admonition(inner_url, title)



def youtube_video_admonition(inner_url, title='Video'):
    return f'''??? video "{title}"

    <div style="position: relative; padding-bottom: 56.25%; height: 0; overflow: hidden;">
        <iframe src="{inner_url}" title="YouTube video player" frameborder="0" allow="accelerometer; autoplay; clipboard-write; encrypted-media; gyroscope; picture-in-picture; web-share" referrerpolicy="strict-origin-when-cross-origin" allowfullscreen style="position: absolute; top: 0; left: 0; width: 100%; height: 100%;"></iframe>
    </div>'''


def create_task(title="Aufgabe",
                question="⚠QUESTION_TEXT_MISSING⚠",
                solution="",
                tip="",
                difficulty=0,
                difficulty_icon='🌶',
                collapsed=False,
                solution_video=None,
                question_video=None,
                show_solution=True):
    difficulty_icons = difficulty * difficulty_icon + (" " if difficulty else "")
    collapsed_symbol = "" if collapsed else "+"

    result = f'???{collapsed_symbol} question "{difficulty_icons}{title}"\n'
    if question_video:
        result += add_tabs(youtube_video_admonition(question_video))

    result += add_tabs(question)
    if tip:
        result += add_tabs(f'??? info "Tipp"\n') + add_tabs(tip, 2)
    if solution and show_solution:
        result += add_tabs(f'??? success "Lösung"\n')
        if solution_video:
            result += add_tabs(youtube_video_admonition(solution_video, "Lösungsvideo"), 2)
        result += add_tabs(solution, 2)
    return result


def add_tabs(text, tabs=1):
    return ('\n' + text).replace('\n', '\n' + '\t' * tabs)
