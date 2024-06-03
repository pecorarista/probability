from pathlib import Path
import queue

DELIM = '\t'

def main() -> None:
    q = queue.Queue()
    gloss_dirname = Path('gloss')
    for name in ['laplace', 'kolmogorov']:
        input_filename = gloss_dirname.joinpath(f'{name}.csv')
        output_filename = gloss_dirname.joinpath(f'{name}.tex')
        with input_filename.open(mode='r') as r, output_filename.open(mode='w') as w:
            for (i, line) in enumerate(r):
                if len(line.strip()) == 0:
                    (fr, pr, en, trans) = zip(*q.queue)
                    s = f'''
    \\trigloss{{{' '.join(fr).strip()}}}
              {{{' '.join(pr).strip()}}}
              {{{' '.join(en).strip()}}}
              {{{' '.join(trans).strip()}}}\n'''
                    w.write(s)
                    q = queue.Queue()
                else:
                    try:
                        (fr, pr, en, trans) = line.replace('\n', '').split(DELIM)
                        q.put((fr, pr, en, trans))
                    except ValueError:
                        print(name, i, line)
                        return


if __name__ == '__main__':
    main()
