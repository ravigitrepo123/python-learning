import re
from pathlib import Path


def parse_qs(infile: Path):
    text = infile.read_text(encoding='utf-8', errors='ignore').splitlines()
    questions = []
    current = None
    state = None
    for line in text:
        m = re.match(r'^\s*Q\)\s*(.*)', line)
        if m:
            if current:
                questions.append(current)
            current = {'q': m.group(1).strip(), 'a_lines': []}
            state = 'q'
            continue
        m2 = re.match(r'^\s*S\)\s*(.*)', line, re.I)
        if m2 and current:
            state = 'a'
            first = m2.group(1)
            if first:
                current['a_lines'].append(first)
            continue
        if current and state == 'a':
            current['a_lines'].append(line.rstrip())

    if current:
        questions.append(current)
    return questions


def _slugify(s: str) -> str:
    s = s.strip().lower()
    # replace spaces with hyphens, remove invalid chars
    s = re.sub(r"[^a-z0-9\s-]", "", s)
    s = re.sub(r"[\s]+", "-", s)
    s = re.sub(r"-+", "-", s)
    return s


def build_md(questions, outfile: Path):
    with outfile.open('w', encoding='utf-8') as f:
        f.write('# Interview Questions — One Liners\n\n')
        f.write('## Table of Contents\n\n')
        for i, q in enumerate(questions, 1):
            title = q['q'] or f'Question {i}'
            title_safe = title.replace('[', '\\[').replace(']', '\\]')
            slug = _slugify(title)
            f.write(f'- [{title_safe}](#{slug})\n')
        f.write('\n---\n\n')

        for i, q in enumerate(questions, 1):
            title = q['q'] or ''
            slug = _slugify(title or f'question-{i}')
            f.write(f'## {title}\n\n')
            f.write('**Answer:**\n\n')
            if q['a_lines']:
                # trim leading/trailing empty lines
                lines = q['a_lines'][:]
                while lines and lines[0].strip() == '':
                    lines.pop(0)
                while lines and lines[-1].strip() == '':
                    lines.pop()
                if all(line.strip() == '' for line in lines):
                    f.write('_No answer provided._\n\n')
                else:
                    f.write('```text\n')
                    for line in lines:
                        f.write(line + '\n')
                    f.write('```\n\n')
            else:
                f.write('_No answer provided._\n\n')
            f.write('[Back to Table of Contents](#table-of-contents)\n\n')


def main():
    infile = Path(r'd:\python-learning\Interview_questions_one_liners')
    outfile = Path(r'd:\python-learning\Interview_questions_one_liners.md')
    if not infile.exists():
        print('Input file not found:', infile)
        return
    questions = parse_qs(infile)
    build_md(questions, outfile)
    print('Wrote', outfile)


if __name__ == '__main__':
    main()
