import os

def rename_ds9(season_path, snum):
    os.chdir(season_path)
    i = 0
    snum = str(snum)
    for file in os.listdir():
        if i == 0:
            src = file
            dst = 'Star Trek Deep Space 9 - s0' + snum + 'e01-e02 -' + src[10:]
            os.rename(src, dst)
            i += 1
        else:

            src = file
            ep = int(file[8:10])
            ep += 1
            if ep < 10:
                ep = '0'+ str(ep)
            else:
                ep = str(ep)
            dst = 'Star Trek Deep Space 9 - s0' + snum + 'e' + ep + ' -' + src[10:]
            os.rename(src, dst)


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    rename_ds9('D:\downloads from line\Star Trek Deep Space 9\DS9 S04 AI_Upscale_1080p+',4)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
