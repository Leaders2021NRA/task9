# task9

сайт конкурса: https://lk.leaders2021.innoagency.ru

лекция по работе с yandex cloud: https://yandex.zoom.us/rec/share/JPnSYZvGSqe9Vl4n4vRZjA2lZ2wlGaEf4UEQNi_IhwFuNqNoLCFCloB6xZS40ju-.04aF7yBoZ--n298t

TODO:
 - добавить другие форматы для перевода в jpg
 - сделать отдельный перевод в jpeg и запускать сразу на jpg (постоянный перевод всего датасета занимаеи много времени)
 - добавить блюр вместо красных рамочек
 - поднять веб морду
 - работа с таблицами сейчас не айс - надо жумать как это исправить https://levelup.gitconnected.com/text-extraction-from-a-table-image-using-pytesseract-and-opencv-3342870691ae
 - не выделать если школа, орден, медаль и тп
 - проверить thresshold при определение. текста в рамках в ocr
 - попробовать другие алгоритмы ocr
 - при распознавании картинки "нормализовать ее" (функции из https://nanonets.com/blog/ocr-with-tesseract/)

venv :
conda activate moshack
ipython kernel install --name "moshack" --user
