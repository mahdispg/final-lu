توضیح crud.py:
این کد، مجموعه‌ای از توابع CRUD (Create, Read, Update, Delete) را برای مدیریت جداول دانشجو (Student)، استاد (Professor) و درس (Course) در پایگاه داده ارائه می‌دهد. در اینجا توضیح خط به خط این کد آمده است:
from sqlalchemy.orm import Session
import sys
from pathlib import Path
sys.path[0] = str(Path(sys.path[0]).parent)

from project import models , schemas

from sqlalchemy.orm import Session: ماژول Session را از sqlalchemy.orm وارد می‌کند که برای مدیریت نشست‌های پایگاه داده استفاده می‌شود.
from pathlib import Path: این‌ها برای تنظیم مسیر سیستم استفاده می‌شوند تا مطمئن شوند که ماژول‌های پروژه به درستی وارد می‌شوند.
from project import models , schemas: مدل‌ها و اسکیماهای پروژه را وارد می‌کند.

توابع مرتبط با جدول دانشجو student:

تابع get_student:
این تابع یک شناسه دانشجو (student_id) را می‌گیرد و دانشجوی مربوطه را از پایگاه داده واکشی می‌کند.

تابع create_student:
این تابع یک شیء schemas.Student را می‌گیرد و یک رکورد جدید دانشجو را در پایگاه داده ایجاد می‌کند.

تابع removestudent:
این تابع یک شناسه دانشجو (Student_id) را می‌گیرد و دانشجوی مربوطه را از پایگاه داده حذف می‌کند.

تابع update_student:
این تابع یک شناسه دانشجو (student_id) و یک شیء models.Student را می‌گیرد و اطلاعات دانشجوی مربوطه را به‌روزرسانی می‌کند.

توابع مرتبط با استاد professor:

تابع get_professor:
این تابع یک شناسه استاد (Professor_id) را می‌گیرد و استاد مربوطه را از پایگاه داده واکشی می‌کند.

تابع create_professor:
این تابع یک شیء schemas.Professor را می‌گیرد و یک رکورد جدید استاد را در پایگاه داده ایجاد می‌کند.

تابع update_professor:
این تابع یک شیء schemas.Professor را می‌گیرد و یک رکورد جدید استاد را در پایگاه داده ایجاد می‌کند.

تابع removeprofessor:
این تابع یک شناسه استاد (Professor_id) را می‌گیرد و استاد مربوطه را از پایگاه داده حذف می‌کند

توابع مرتبط با جدول درس course:

تابع get_course:
این تابع یک شناسه درس (Course_id) را می‌گیرد و درس مربوطه را از پایگاه داده واکشی می‌کند.

تابع create_course:
این تابع یک شیء schemas.Course را می‌گیرد و یک رکورد جدید درس را در پایگاه داده ایجاد می‌کند.

تابع update_course:
این تابع یک شناسه درس (course_id) و یک شیء models.Course را می‌گیرد و اطلاعات درس مربوطه را به‌روزرسانی می‌کند.

تابع removecourse:
این تابع یک شناسه درس (Course_id) را می‌گیرد و درس مربوطه را از پایگاه داده حذف می‌کند.

توضیح database.py:
این کد تنظیمات ابتدایی برای اتصال به پایگاه داده SQLite و ایجاد نشست‌های پایگاه داده با استفاده از SQLAlchemy را نشان می‌دهد. در اینجا توضیح خط به خط این کد آمده است:
وارد کردن ماژول‌ها:
from sqlalchemy import create_engine: تابع create_engine را از SQLAlchemy وارد می‌کند که برای ایجاد یک اتصال به پایگاه داده استفاده می‌شود.
from sqlalchemy.ext.declarative import declarative_base: تابع declarative_base را وارد می‌کند که برای تعریف مدل‌های پایگاه داده استفاده می‌شود.
from sqlalchemy.orm import sessionmaker: کلاس sessionmaker را وارد می‌کند که برای ایجاد نشست‌های پایگاه داده استفاده می‌شود.

تعریف آدرس پایگاه داده:
SQLALCHEMY_DATABASE_URL = "sqlite:///./sql_app.db"
این خط آدرس پایگاه داده را تعیین می‌کند. در اینجا، یک پایگاه داده SQLite با نام sql_app.db در دایرکتوری فعلی ایجاد یا استفاده می‌شود.
"sqlite:///./sql_app.db":
sqlite:///: نشان‌دهنده این است که از SQLite به عنوان پایگاه داده استفاده می‌شود.
./sql_app.db: مسیر فایل پایگاه داده که در دایرکتوری فعلی قرار دارد.

ایجاد موتور پایگاه داده:
engine = create_engine(
    SQLALCHEMY_DATABASE_URL, connect_args={"check_same_thread": False}
)
create_engine: این تابع برای ایجاد یک موتور پایگاه داده استفاده می‌شود که وظیفه مدیریت اتصالات به پایگاه داده را بر عهده دارد.
SQLALCHEMY_DATABASE_URL: آدرس پایگاه داده که در مرحله قبل تعریف شد.
connect_args={"check_same_thread": False}: این گزینه به SQLite اجازه می‌دهد که چندین رشته (thread) به طور همزمان به یک پایگاه داده متصل شوند. این تنظیم خاص برای SQLite است و برای دیگر پایگاه‌های داده لازم نیست.
ایجاد کارخانه نشست (Session Factory):
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
sessionmaker: کلاس sessionmaker برای ایجاد کارخانه نشست استفاده می‌شود. این کارخانه وظیفه ایجاد نشست‌های پایگاه داده را بر عهده دارد.
autocommit=False: این گزینه به طور خودکار تغییرات را در پایگاه داده اعمال نمی‌کند و نیاز به فراخوانی دستی commit دارد.
autoflush=False: این گزینه مانع از ارسال خودکار تغییرات به پایگاه داده قبل از هر کوئری می‌شود.
bind=engine: موتور پایگاه داده‌ای که نشست‌ها باید به آن متصل شوند را مشخص می‌کند.

ایجاد کلاس پایه برای مدل‌ها:
Base = declarative_base()
declarative_base(): این تابع یک کلاس پایه ایجاد می‌کند که همه مدل‌های پایگاه داده باید از آن ارث‌بری کنند. این کلاس پایه شامل تمام متادیتا (metadata) مورد نیاز برای SQLAlchemy است تا بتواند جداول پایگاه داده را ایجاد کند.
این کد به طور کلی تنظیمات اولیه برای کار با پایگاه داده SQLite با استفاده از SQLAlchemy را فراهم می‌کند.

توضیح dockerfile:
ین کد یک فایل Dockerfile است که برای ساخت یک کانتینر Docker استفاده می‌شود. خط به خط این فایل را توضیح می‌دهم:

FROM python:3.12.3
این خط بیان می‌کند که از تصویر پایه python:3.12.3 استفاده شود. این تصویر شامل محیط اجرای Python نسخه 3.12.3 است.

WORKDIR /var/www
این خط دایرکتوری کاری را به /var/www تغییر می‌دهد. این بدان معناست که دستورات بعدی در این دایرکتوری اجرا خواهند شد.

COPY /course/requirements.txt .
این خط فایل requirements.txt را از مسیر محلی /course/ به دایرکتوری کاری جاری در داخل کانتینر (که /var/www است) کپی می‌کند.

RUN pip install -r requirements.txt
این خط دستور pip install -r requirements.txt را اجرا می‌کند که کتابخانه‌های مورد نیاز پروژه که در فایل requirements.txt مشخص شده‌اند را نصب می‌کند.

COPY course /var/www/
این خط دایرکتوری course را از مسیر محلی به دایرکتوری کاری /var/www در داخل کانتینر کپی می‌کند. این شامل همه فایل‌ها و زیرپوشه‌های داخل دایرکتوری course است.

CMD ["fastapi", "run", "main.py"]
این خط دستور شروع کانتینر را مشخص می‌کند. در اینجا، از FastAPI برای اجرای فایل main.py استفاده می‌شود. CMD تعیین می‌کند که وقتی کانتینر اجرا می‌شود، چه دستوری باید اجرا شود.
به طور خلاصه، این Dockerfile یک محیط Python 3.12.3 ایجاد می‌کند، وابستگی‌ها را از فایل requirements.txt نصب می‌کند، کد پروژه را به داخل کانتینر کپی می‌کند، و سپس FastAPI را برای اجرای برنامه Python (main.py) راه‌اندازی می‌کند