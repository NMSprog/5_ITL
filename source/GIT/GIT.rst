***
GIT
***

Клонирование репозитория в локальную папку:

.. code:: GIT
    
    git clone https://github.com/Автор_Username/Pylessons.git J:\GIT\IT_Lessons

Создание нового репозитория на GitHub:

    Перейдите на GitHub и войдите в свою учетную запись.
    Создайте новый репозиторий с именем IT_Lessons.
    При создании выберите "Public" или "Private" в зависимости от ваших предпочтений.
    
Привязка локального репозитория к вашему GitHub репозиторию:

.. code:: GIT

    cd J:\GIT\IT_Lessons - переход в деректорию

    git remote remove origin - Удаляет удалённый репозиторий с именем origin из вашего локального Git-репозитория. Заменить URL удалённого репозитория

    git remote add origin https://github.com/Ваш_Username/IT_Lessons.git - Замените Ваш_Username на ваш реальный GitHub username.

    git push -u origin master - Отправить все изменения в ваш новый репозиторий на GitHub