# encoding: utf-8
from argparse import ArgumentParser
from subprocess import Popen, PIPE
import re
import matplotlib.pyplot as plt


def parse_log(logtext):
    epoch = []
    loss = []
    acc = []
    val_loss = []
    val_acc = []

    logs = logtext.split('\n')
    for log in logs:
        m = re.search("^Epoch (\d+)/\d+", log)
        if m:
            epoch.append(int(m.group(1)))
        else:
            m = re.search("\d+/\d+ \[==============================\] - \d+s", log)
            if m:
                m_loss = re.search(" loss: ([\d\.]+)", log)
                m_acc = re.search(" acc: ([\d\.]+)", log)
                m_val_loss = re.search(" val_loss: ([\d\.]+)", log)
                m_val_acc = re.search(" val_acc: ([\d\.]+)", log)
                if m_loss:
                    loss.append(m_loss.group(1))
                else:
                    loss.append(None)
                if m_acc:
                    acc.append(m_acc.group(1))
                else:
                    acc.append(None)
                if m_val_loss:
                    val_loss.append(m_val_loss.group(1))
                else:
                    val_loss.append(None)
                if m_val_acc:
                    val_acc.append(m_val_acc.group(1))
                else:
                    val_acc.append(None)
    data = {}
    data['epoch'] = epoch
    data['loss'] = loss
    data['acc'] = acc
    data['val_loss'] = val_loss
    data['val_acc'] = val_acc

    return data


def main():
    parser = ArgumentParser()
    parser.add_argument('--output', '-o', action='store', type=str, help='output filename')
    parser.add_argument('--input', '-i', action='store', type=str, help='input filename')
    parser.add_argument('--clipboard', action='store_true', help='read log from clipboard')
    args = parser.parse_args()

    if args.clipboard:
        p = Popen(['pbpaste'], stdout=PIPE, stderr=PIPE)
        out, _err = p.communicate()
        log = out.decode('utf-8') # bytes -> str
    elif args.input:
        with open(args.input) as f:
            log = f.read()
    else:
        print("Input source is not specified. Use --input or --clipboard.")
        exit()
    # print(log)
    data = parse_log(log)
    print(data)

    if len(data['epoch']) == 0:
        return

    # Plot training loss
    plt.subplot(2, 2, 1)
    plt.title("training loss")
    if len(data['epoch']) < 4:
        plt.xticks(range(min(data['epoch']), max(data['epoch']) + 1))
    plt.ylim(0, 1.1)
    plt.plot(data['epoch'], data['loss'])

    # Plot training accuracy
    plt.subplot(2, 2, 2)
    plt.title("training accuracy")
    if len(data['epoch']) < 4:
        plt.xticks(range(min(data['epoch']), max(data['epoch']) + 1))
    plt.ylim(0, 1.1)
    plt.plot(data['epoch'], data['acc'])

    # Plot validation loss
    plt.subplot(2, 2, 3)
    plt.title("validation loss")
    if len(data['epoch']) < 4:
        plt.xticks(range(min(data['epoch']), max(data['epoch']) + 1))
    plt.ylim(0, 1.1)
    plt.plot(data['epoch'], data['val_loss'])

    # Plot validation accuracy
    plt.subplot(2, 2, 4)
    plt.title("validation accuracy")
    if len(data['epoch']) < 4:
        plt.xticks(range(min(data['epoch']), max(data['epoch']) + 1))
    plt.ylim(0, 1.1)
    plt.plot(data['epoch'], data['val_acc'])

    plt.subplots_adjust(hspace=0.3)
    if args.output:
        plt.savefig(args.output)
    else:
        plt.show()


if __name__ == '__main__':
    main()
