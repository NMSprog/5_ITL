***************
Сайт IT_Lessons
***************


Боковое меню строится в файле index.rst

Если в файле .rst есть структура:

.. code:: 

    Search
    ======
    Overview
    --------
    Details
    ~~~~~~~

При :maxdepth: 1 → в оглавлении будет только "Search".
При :maxdepth: 2 → будет "Search" и "Overview".
При :maxdepth: 3 → будет "Search", "Overview", "Details".


Добавление в меню.

*Вариант №1*

1. Создание новой папки в папке source
2. Создание нового файла в папке с расширением .rst

:: 

    ***************
    Сайт IT_Lessons
    ***************
    
    Количество * должно соответствовать с длиной строки.

3. Добавление в меню сайта в файле index.rst 

:: 

    .. toctree::
        :caption: Консоли
        :maxdepth: 2
    
        Сonsole/Сonsole

*Вариант №2*

1. Добавление в меню сайта в файле index.rst 

:: 

    ----

    #################
    :ref:`docker`
    #################

    .. include:: text/00-index/010-docker_description.rst

    .. toctree::
    :hidden:
    :maxdepth: 1

    index-01-docker.rst

    ----

2. Создание файла index-01-docker.rst в котором указана папка с фалами (текстом)

:: 

    .. toctree::
        :maxdepth: 2
        :glob:

        text/01-docker/*

3. Содержимое папки 

::
    011_chapter1.rst
    031_chapter3.rst
    041_chapter4.rst
    051_chapter5.rst
    061_chapter6.rst
    991_links.rst