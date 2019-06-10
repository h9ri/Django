# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey has `on_delete` set to the desired behavior.
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Activate(models.Model):
    id = models.CharField(primary_key=True, max_length=7)
    number_of_barred = models.DecimalField(db_column='NUMBER_OF_BARRED', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    number_of_unbarred = models.DecimalField(db_column='NUMBER_OF_UNBARRED', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    number_of_months_barred = models.DecimalField(db_column='NUMBER_OF_MONTHS_BARRED', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    total_monthly_bill = models.DecimalField(db_column='TOTAL_MONTHLY_BILL', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    total_no_of_bills = models.IntegerField(db_column='TOTAL_NO_OF_BILLS', blank=True, null=True)  # Field name made lowercase.
    std_bill = models.DecimalField(db_column='STD_BILL', max_digits=31, decimal_places=13, blank=True, null=True)  # Field name made lowercase.
    age_on_network = models.CharField(db_column='AGE_ON_NETWORK', max_length=28, blank=True, null=True)  # Field name made lowercase.
    age = models.DecimalField(db_column='AGE', max_digits=18, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    gender_m = models.IntegerField(db_column='GENDER_M', blank=True, null=True)  # Field name made lowercase.
    gender_f = models.IntegerField(db_column='GENDER_F', blank=True, null=True)  # Field name made lowercase.
    gender_u = models.IntegerField(db_column='GENDER_U', blank=True, null=True)  # Field name made lowercase.
    device_type_huawei = models.IntegerField(db_column='DEVICE_TYPE_HUAWEI', blank=True, null=True)  # Field name made lowercase.
    device_type_iphone = models.IntegerField(db_column='DEVICE_TYPE_IPHONE', blank=True, null=True)  # Field name made lowercase.
    device_type_oppo = models.IntegerField(db_column='DEVICE_TYPE_OPPO', blank=True, null=True)  # Field name made lowercase.
    device_type_samsung = models.IntegerField(db_column='DEVICE_TYPE_SAMSUNG', blank=True, null=True)  # Field name made lowercase.
    state_johor = models.IntegerField(db_column='STATE_JOHOR', blank=True, null=True)  # Field name made lowercase.
    state_kedah = models.IntegerField(db_column='STATE_KEDAH', blank=True, null=True)  # Field name made lowercase.
    state_kelantan = models.IntegerField(db_column='STATE_KELANTAN', blank=True, null=True)  # Field name made lowercase.
    state_melaka = models.IntegerField(db_column='STATE_MELAKA', blank=True, null=True)  # Field name made lowercase.
    state_negeri_sembilan = models.IntegerField(db_column='STATE_NEGERI SEMBILAN', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    state_pahang = models.IntegerField(db_column='STATE_PAHANG', blank=True, null=True)  # Field name made lowercase.
    state_perak = models.IntegerField(db_column='STATE_PERAK', blank=True, null=True)  # Field name made lowercase.
    state_perlis = models.IntegerField(db_column='STATE_PERLIS', blank=True, null=True)  # Field name made lowercase.
    state_pulau_pinang = models.IntegerField(db_column='STATE_PULAU PINANG', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    state_sabah = models.IntegerField(db_column='STATE_SABAH', blank=True, null=True)  # Field name made lowercase.
    state_sarawak = models.IntegerField(db_column='STATE_SARAWAK', blank=True, null=True)  # Field name made lowercase.
    state_selangor = models.IntegerField(db_column='STATE_SELANGOR', blank=True, null=True)  # Field name made lowercase.
    state_terengganu = models.IntegerField(db_column='STATE_TERENGGANU', blank=True, null=True)  # Field name made lowercase.
    state_wp_kuala_lumpur = models.IntegerField(db_column='STATE_WP KUALA LUMPUR', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    number_of_devices = models.IntegerField(db_column='NUMBER_OF_DEVICES', blank=True, null=True)  # Field name made lowercase.
    rateplan_postpaid_p50 = models.IntegerField(db_column='RATEPLAN_Postpaid P50', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rateplan_postpaid_p70 = models.IntegerField(db_column='RATEPLAN_Postpaid P70', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rateplan_postpaid_p98 = models.IntegerField(db_column='RATEPLAN_Postpaid P98', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rateplan_postpaid_plan_p139 = models.IntegerField(db_column='RATEPLAN_Postpaid Plan P139', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rateplan_postpaid_plan_p79 = models.IntegerField(db_column='RATEPLAN_Postpaid Plan P79', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rateplan_postpaid_plan_p99 = models.IntegerField(db_column='RATEPLAN_Postpaid Plan P99', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    rateplan_i130 = models.IntegerField(db_column='RATEPLAN_i130', blank=True, null=True)  # Field name made lowercase.
    rateplan_i60 = models.IntegerField(db_column='RATEPLAN_i60', blank=True, null=True)  # Field name made lowercase.
    rateplan_i90 = models.IntegerField(db_column='RATEPLAN_i90', blank=True, null=True)  # Field name made lowercase.
    rateplan_others = models.IntegerField(db_column='RATEPLAN_OTHERS', blank=True, null=True)  # Field name made lowercase.
    payment_mode_cash = models.IntegerField(db_column='PAYMENT_MODE_Cash', blank=True, null=True)  # Field name made lowercase.
    payment_mode_cheque = models.IntegerField(db_column='PAYMENT_MODE_Cheque', blank=True, null=True)  # Field name made lowercase.
    payment_mode_credit_card = models.IntegerField(db_column='PAYMENT_MODE_Credit Card', blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    payment_mode_voucher = models.IntegerField(db_column='PAYMENT_MODE_Voucher', blank=True, null=True)  # Field name made lowercase.
    payment_mode_others = models.IntegerField(db_column='PAYMENT_MODE_OTHERS', blank=True, null=True)  # Field name made lowercase.
    total_amount_paid = models.DecimalField(db_column='TOTAL_AMOUNT_PAID', max_digits=20, decimal_places=2, blank=True, null=True)  # Field name made lowercase.
    number_of_payments = models.IntegerField(db_column='NUMBER_OF_PAYMENTS', blank=True, null=True)  # Field name made lowercase.
    number_of_months_payment = models.IntegerField(db_column='NUMBER_OF_MONTHS_PAYMENT', blank=True, null=True)  # Field name made lowercase.
    monthly_average_payment = models.DecimalField(db_column='MONTHLY_AVERAGE_PAYMENT', max_digits=23, decimal_places=5, blank=True, null=True)  # Field name made lowercase.
    service_bis20 = models.DecimalField(db_column='SERVICE_BIS20', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    service_bisd = models.DecimalField(db_column='SERVICE_BISD', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    service_bos = models.DecimalField(db_column='SERVICE_BOS', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    service_clir = models.DecimalField(db_column='SERVICE_CLIR', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    service_physical_bill_stmt_itemisedrm3 = models.DecimalField(db_column='SERVICE_Physical Bill Stmt-ItemisedRM3', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_rm5_u_sms_plus = models.DecimalField(db_column='SERVICE_RM5 U SMS Plus', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_rm5_u_talk_plus = models.DecimalField(db_column='SERVICE_RM5 U Talk Plus', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_rm8_sms_plus = models.DecimalField(db_column='SERVICE_RM8 SMS Plus', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_rm8_talk_plus = models.DecimalField(db_column='SERVICE_RM8 Talk Plus', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase. Field renamed to remove unsuitable characters.
    service_other = models.DecimalField(db_column='SERVICE_OTHER', max_digits=2, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    total_no_of_services = models.DecimalField(db_column='TOTAL_NO_OF_SERVICES', max_digits=4, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    month_used_services = models.DecimalField(db_column='MONTH_USED_SERVICES', max_digits=3, decimal_places=1, blank=True, null=True)  # Field name made lowercase.
    monthly_avg_service = models.DecimalField(db_column='MONTHLY_AVG_SERVICE', max_digits=21, decimal_places=3, blank=True, null=True)  # Field name made lowercase.
    age_survive = models.CharField(db_column='AGE_SURVIVE', max_length=27, blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'Activate'


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthUser(models.Model):
    password = models.CharField(max_length=128)
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=30)
    last_name = models.CharField(max_length=150)
    email = models.CharField(max_length=254)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'auth_user'


class AuthUserGroups(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_groups'
        unique_together = (('user', 'group'),)


class AuthUserUserPermissions(models.Model):
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_user_user_permissions'
        unique_together = (('user', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthUser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'

