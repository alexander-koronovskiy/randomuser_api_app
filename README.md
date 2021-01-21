��������:

���������� ��� �������������� � ������� API: https://randomuser.me/
�������� �������� ���������� ������������ �� ���� ������� web �������� c ����� ��� ����� ���������� �������, ������� ���������� ��������� � API, � ����� ���������� � �������� ��������� ��������.


����������:

1) �� �������� ��������� ��������� ����������: ��� ��������, ���, �������, ����� ��������, email, ����� ����������.

2) ��� ������� �� ������� - ������� ��� ������� "UPDATE USER" ������ ��� ������� ��������� ������� �� ���� ������.

3) ���� ��� ����� ���������� ������� (��������� � ����� web-��������) ��������� � ������� ���������� � ������������� �� ���� ������. ���������� ����� � ������� ������������ ��������� � ���������� ������ �� 0 �� 10.

4) ������ ��� ��� ������ ���������� - ��� ���� ������ �����������.

5) ��� ������� "LOAD DATA" ���������� ���������� json-����� � �����������, ������������ � ���� ������.


����������� ����������:

1) ������������ ���������� ��� ������ � �� � ��������: Flask, Sql lite, peewee.

2) ����� ������ ��������, �� ��������� 10 ��������� ����� �� API.

3) ���������� ��������� ���������� ������ docker ����������.


������ ���������:

1) �������� ������ ����������: $ docker build -t my_app .
2) ������ ���������� �� ���������� ������: $ docker run -p 5000:5000 -t my_app
3) ������� �� ������ � ��������: /localhost:5000


������������:

�� ��������� ������ ���� ���������� python

1) $ pip install -r requirements.txt
2) ������� � �����������, � ������� ��������� �����: $ cd app
3) $ pytest


� ����������:

��������� � ������������ �� ������: http://homepage/user_id.
