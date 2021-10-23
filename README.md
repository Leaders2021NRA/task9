# task9

Решение команды NRA задачи 9 конкурса https://lk.leaders2021.innoagency.ru

MVP содержит:
 - конвертация pdf->jpg
 - распознавание текста в jpg
 - распозвание NER в тексте
 - веб сервис


Для работы сервиса рекомендуется поставить виртуальное окружение:
```
conda create -n moshack python=3.6
conda install matplotlib pdf2image pandas numpy scikit-learn tqdm opencv-python pytesseract natasha
```

Установить окружение в jupyter notebook:
```
ipython kernel install --name "moshack" --user
```

TODO (внутреннее):
 - сделать отдельный перевод в jpg и запускать сразу на jpg (постоянный перевод всего датасета занимает много времени)
 - работа с таблицами сейчас не айс - надо думать как это исправить https://levelup.gitconnected.com/text-extraction-from-a-table-image-using-pytesseract-and-opencv-3342870691ae
 - не выделать если школа, орден, медаль и тп
 - проверить thresshold при определении текста в рамках в ocr
 - попробовать другие алгоритмы ocr
 - при распознавании картинки "нормализовать ее" (функции из https://nanonets.com/blog/ocr-with-tesseract/)
