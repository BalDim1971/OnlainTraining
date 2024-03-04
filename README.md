# Онлайн-обучение
# DRF

## Задание к уроку 24.1

В мире развивается тренд на онлайн-обучение. Но для веб-разработчика важно не 
только обучиться, но и знать, как реализовать платформу для онлайн-обучения. 
Поэтому новая задача касается разработки LMS-системы, в которой каждый желающий
может размещать свои полезные материалы или курсы.

Ранее в проектах мы могли сразу видеть визуальное отображение результата 
разработки, теперь работа будет над SPA веб-приложением и результатом создания 
проекта будет бэкенд-сервер, который возвращает клиенту JSON-структуры.

### Задание 1
Создайте новый Django-проект, подключите DRF в настройках проекта.

### Задание 2
Создайте следующие модели:

1. Пользователь:
- все поля от обычного пользователя, но авторизацию заменить на email;
- телефон;
- город;
- аватарка.

Модель пользователя разместите в приложении users

2. Курс:
- название,
- превью (картинка),
- описание.

3. Урок:
- название,
- описание,
- превью (картинка),
- ссылка на видео.

Урок и курс - это связанные между собой сущности. Уроки складываются в курс, 
в одном курсе может быть много уроков. 
Реализуйте связь между ними.

Модель курса и урока разместите в отдельном приложении. Название для приложения
выбирайте такое, чтобы оно описывало то, с какими сущностями приложение 
работает. Например, lms или materials - отличные варианты.

### Задание 3
Опишите CRUD для моделей курса и урока. Для реализации CRUD для курса 
используйте Viewsets, а для урока - Generic-классы.

Для работы контроллеров опишите простейшие сериализаторы.

При реализации CRUD для уроков реализуйте все необходимые операции 
(получение списка, получение одной сущности, создание, изменение и удаление).

Работу каждого эндпоинта необходимо проверять с помощью Postman.
Также на данном этапе работы мы не заботимся о безопасности и не закрываем от 
редактирования объекты и модели даже самой простой авторизацией.


## Задание к уроку 24.2

Продолжаем развивать проект LMS системы для более удобной работы с ним.

### Задание 1
Для модели курса добавьте в сериализатор поле вывода количества уроков. 
Поле реализуйте с помощью SerializerMethodField()

### Задание 2
Добавьте новую модель в приложение users:

1. Платежи
- пользователь,
- дата оплаты,
- оплаченный курс или урок,
- сумма оплаты,
- способ оплаты: наличные или перевод на счет.

Поля пользователь, оплаченный курс и отдельно оплаченный урок
должны быть ссылками на соответствующие модели.

Запишите в таблицу, соответствующую этой модели данные через инструмент 
фикстур или кастомную команду.

Если вы забыли как работать с фикстурами или кастомной командой - можете 
вернуться к уроку 20.1 "Работа с ORM в Django" чтобы вспомнить материал.

### Задание 3
Для сериализатора для модели курса реализуйте поле вывода уроков. Вывод 
реализуйте с помощью сериализатора для связанной модели.

Один сериализатор должен выдавать и количество уроков курса и информацию 
по всем урокам курса одновременно.

### Задание 4
Настроить фильтрацию для эндпоинта вывода списка платежей с возможностями:
- менять порядок сортировки по дате оплаты,
- фильтровать по курсу или уроку,
- фильтровать по способу оплаты.

#### Дополнительное задание
Для профиля пользователя сделайте вывод истории платежей, расширив 
сериализатор для вывода списка платежей


## Задание к уроку 25.1 Права доступа в DRF

Продолжаем работать с проектом. Переходим к описанию прав доступа и 
авторизации пользователей.

### Контекст: зачем решать подобные задачи
Для разграничения прав доступа в любом сервисе используются настройки, которые 
в DRF предоставляет пакет permissions. Задача разграничения прав доступа — 
очень частая в рамках работы над растущими и развивающимися проектами.

### Задание 1
Реализуйте CRUD для пользователей, в том числе регистрацию пользователей, 
настройте в проекте использование JWT-авторизации и закройте каждый эндпоинт 
авторизацией.
Эндпоинты для авторизации и регистрации должны остаться доступны для 
неавторизованных пользователей.

### Задание 2
Заведите группу модераторов и опишите для нее права работы с любыми уроками и 
курсами, но без возможности их удалять и создавать новые. Заложите функционал 
такой проверки в контроллеры.

### Задание 3
Опишите права доступа для объектов таким образом, чтобы пользователи, которые 
не входят в группу модераторов, могли видеть, редактировать и удалять только 
свои курсы и уроки.

### Дополнительное задание урока 25.1
Для профиля пользователя введите ограничения, чтобы авторизованный пользователь
мог просматривать любой профиль, но редактировать только свой. При этом для 
просмотра чужого профиля должна быть доступна только общая информация, 
в которую не входят: пароль, фамилия, история платежей.


### Критерии решения каждой домашней работы:
Результат выполнения всего задания залит в github.com и сдан в виде ссылки 
на репозиторий
Примечание: дополнительные задания помеченные звездочкой желательны, но 
не обязательны к выполнению.


## Задание к уроку 25.2 Валидация, пагинация и тесты

Продолжаем работать с проектом.  Добавляем проверку передаваемых данных и 
тестируем получившийся код.

### Контекст: зачем решать подобные задачи
Когда пользователи вводят информацию, то из-за невнимательности или по незнанию 
могут ошибиться. Поэтому введенные данные всегда нужно валидировать. А для 
увеличения скорости работы пользователя необходимо дробить информацию и 
выводить ее по страницам. Помимо улучшений в коде, важно проверять, что код 
работает верно, и писать тесты.

### Задание 1
Для сохранения уроков и курсов реализуйте дополнительную проверку на отсутствие
в материалах ссылок на сторонние ресурсы, кроме youtube.com.
То есть ссылки на видео можно прикреплять в материалы, а ссылки на сторонние 
образовательные платформы или личные сайты — нельзя.
#### Рекомендация:
Создайте отдельный файл validators.py, реализуйте валидатор, проверяющий 
ссылку, которую пользователь хочет записать в поле урока с помощью класса или 
функции.
Интегрируйте валидатор в сериализатор.
Если вы используете функцию-валидатор — указанием валидаторов для поля 
сериализатора validators=[ваш_валидатор].
Если вы используете класс-валидатор — указанием валидаторов в
class Meta:
validators = [ваш_валидатор(field='поле_которое_валидируем')].

### Задание 2
Добавьте модель подписки на обновления курса для пользователя.
#### Рекомендация:
Модель подписки должна содержать следующие поля: «пользователь» (FK на модель 
пользователя), «курс» (FK на модель курса). Можете дополнительно расширить 
модель при необходимости.

Вам необходимо реализовать эндпоинт для установки подписки пользователя и на 
удаление подписки у пользователя.
#### Рекомендация:
Воспользуйтесь APIView и реализуйте логику метода post, который будет отдавать 
ответ в зависимости от действия.
Пример кода метода post для управления подпиской:

def post(self, *args, **kwargs):
    user = получаем пользователя из self.requests
    course_id = получаем id курса из self.requests.data
    course_item = получаем объект курса из базы с помощью get_object_or_404
    subs_item = получаем объекты подписок по текущему пользователю и курса
	# Если подписка у пользователя на этот курс есть - удаляем ее
    if subs_item.exists():
        ...
        message = 'подписка удалена'
		# Если подписки у пользователя на этот курс нет - создаем ее
    else:
        ...
        message = 'подписка добавлена'
		# Возвращаем ответ в API
    return Response({"message": message})

Зарегистрируйте новый контроллер в url и проверьте его работоспособность 
в Postman. 

При этом при выборке данных по курсу пользователю необходимо присылать признак 
подписки текущего пользователя на курс. То есть давать информацию, подписан 
пользователь на обновления курса или нет.
#### Рекомендация:
Чтобы реализовать это, используйте SerializerMethodField() с соответствующим 
методом или вложенный сериализатор для подписки.

### Задание 3
Реализуйте пагинацию для вывода всех уроков и курсов.
#### Рекомендация:
Пагинацию реализуйте в отдельном файле paginators.py. Можно реализовать один 
или несколько классов пагинатора. Укажите параметры page_size, 
page_size_query_param, max_page_size для класса PageNumberPagination. 
Количество элементов на странице выберите самостоятельно. Интегрируйте 
пагинатор в контроллеры, используя параметр pagination_class.

### Задание 4
Напишите тесты, которые будут проверять корректность работы CRUD уроков и 
функционал работы подписки на обновления курса.
#### Рекомендация:
В тестах используйте метод setUp для заполнения базы данных тестовыми данными. 
Обработайте возможные варианты взаимодействия с контроллерами пользователей с 
разными правами доступа. Для аутентификации пользователей используйте 
self.client.force_authenticate(). Документацию к этому методу можно найти тут: 
https://www.django-rest-framework.org/api-guide/testing/#forcing-authentication.

Сохраните результат проверки покрытия тестами.

### Дополнительное задание *
Напишите тесты на все имеющиеся эндпоинты в проекте.
#### Примечание:
Дополнительное задание, помеченное звездочкой, желательно, но не обязательно 
выполнять.


## Задание к уроку 26.1 Документирование и безопасность

В продолжение работы над проектом необходимо оформить документацию, а также 
поработать со сторонней документацией.

### Контекст: зачем решать подобные задачи
Практически каждый сервис, над которым работают веб-разработчики, требует или
создания документации, или работы с документацией и создания интеграции.

### Декомпозиция задачи
Чтобы выполнить задачу, разработчикам часто приходится декомпозировать ее. 
В этом домашнем задании вам тоже нужно декомпозировать задачу, чтобы успешно 
с ней справиться.

### Задание 1
Подключить и настроить вывод документации для проекта. Убедиться, что каждый 
из реализованных эндпоинтов описан в документации верно, при необходимости 
описать вручную.
Для работы с документацией проекта воспользуйтесь библиотекой drf-yasg или 
drf-spectacular.
Как вручную можно сформировать документацию в drf-yasg можно почитать 
https://drf-yasg.readthedocs.io/en/stable/custom_spec.html, 
в drf-spectacular — https://habr.com/ru/articles/733942/ или 
https://drf-spectacular.readthedocs.io/en/latest/customization.html.

### Задание 2
Подключить возможность оплаты курсов через https://stripe.com/docs/api.
Доступы можно получить напрямую из документации, а также пройти простую 
регистрацию по адресу https://dashboard.stripe.com/register.
Для работы с учебным проектом достаточно зарегистрировать аккаунт и не 
подтверждать его — аккаунт будет находиться в тестовом режиме.
![img.png](img.png)
Для работы с запросами вам понадобится реализовать обращение к эндпоинтам:
https://stripe.com/docs/api/products/create — создание продукта;
https://stripe.com/docs/api/prices/create — создание цены;
https://stripe.com/docs/api/checkout/sessions/create — создание сессии для 
получения ссылки на оплату.
При создании цены и сессии обратите внимание на поля, которые вы передаете в 
запросе. Внимательно изучите значение каждого поля и проанализируйте ошибки 
при их возникновении, чтобы создать корректную запись.
При создании сессии нужно передавать id цены, которая соответствует 
конкретному продукту.
Для тестирования можно использовать номера карт из документации:
https://stripe.com/docs/terminal/references/testing#standard-test-cards.

#### Примечание
Подключение оплаты лучше всего рассматривать как обычную задачу подключения 
к стороннему API.
Основной путь: запрос на покупку → оплата. Статус проверять не нужно.
Каждый эквайринг предоставляет тестовые карты для работы с виртуальными 
деньгами.

#### Подсказка
Необходимо связать данные от сервиса платежей со своим приложением. Все 
взаимодействия с платежным сервисом опишите в сервисных функциях. Сервисные 
функции взаимодействуют с платежным сервисом (Stripe) и отдают ответы в виде 
JSON. Далее результаты работы сервисных функций мы используем в соответствующих
View: при создании платежа в нашей системе мы должны создать продукт, цену и 
сессию для платежа в Stripe, сохранить ссылку на оплату в созданном платеже в 
нашей системе и отдать пользователю в ответе на POST-запрос ссылку на оплату 
или данные о платеже (которые будут включать ссылку на оплату).
При необходимости проверки статуса платежа можно реализовать дополнительную 
View, которая будет обращаться на Session Retrieve 
(https://stripe.com/docs/api/checkout/sessions/retrieve) по id созданной в 
Stripe сессии и отдавать пользователю данные о статусе платежа. Статус платежа 
также можно дополнительно хранить в модели платежей в нашей системе.
Перед созданием сессии необходимо создать продукт и цену. Все эти данные мы 
можем получить из модели платежа (модель платежа связана с продуктом, в 
продукте есть название и цена).
Обратите внимание, что цены при передаче в Strip указываются в копейках (то 
есть текущую цену продукта нужно умножить на 100).

### Дополнительное задание *
Реализуйте проверку статуса с помощью эндпоинта 
https://stripe.com/docs/api/checkout/sessions/retrieve — получение данных о 
сессии по идентификатору.
#### Примечание:
Дополнительное задание, помеченное звездочкой, желательно, но не обязательно 
выполнять.

## Запуск на выполнение курсовой работы

Используется Python 3.12
Описание работ для PyCharm в Windows.

1. Создать и активировать виртуальное окружение.
python -m venv venv
.\venv\Scripts\activate

2. Установить зависимости проекта, указанные в файле requirements.txt
pip install -r requirements.txt 
или средствами PyCharm.

3. Создать файл .env.
Записать в файл настройки, как в шаблоне .env.sample

4. При необходимости создать миграции:
python manage.py makemigrations
Применить миграции
python manage.py migrate

5. Создать суперпользователя
python manage.py csu

6. Для тестового прогона можно использовать файл test.json и users_test.json:
Уточнить тестовые файлы. Работали на первом уроке, на остальных проверить.
python manage.py loaddata test.json
python manage.py loaddata users_test.json

7. Запустить сервер
python manage.py runserver
