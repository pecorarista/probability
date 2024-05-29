from pathlib import Path
import queue

DELIM = '\t'

def main() -> None:
    q = queue.Queue()
    with (
        Path('laplace.csv').open(mode='r') as r,
        Path('gloss.tex').open(mode='w') as w
    ):
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
                    print(i, line)
                    return


if __name__ == '__main__':
    main()
