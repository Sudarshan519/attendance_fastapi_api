"""init

Revision ID: 005cf09e1697
Revises: 8fb2d0b7f4cc
Create Date: 2023-08-29 19:57:23.662922

"""
from alembic import op
import sqlalchemy as sa
from sqlalchemy.dialects import postgresql

# revision identifiers, used by Alembic.
revision = '005cf09e1697'
down_revision = '8fb2d0b7f4cc'
branch_labels = None
depends_on = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('businessleavedays',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyid', sa.Integer(), nullable=True),
    sa.Column('days', sa.Enum('SUNDAY', 'MONDAY', 'TUESDAY', 'WEDNESDAY', 'THURSDAY', 'FRIDAY', 'SATURDAY', name='businessleaveday'), nullable=True),
    sa.ForeignKeyConstraint(['companyid'], ['companymodel.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_businessleavedays_id'), 'businessleavedays', ['id'], unique=False)
    op.create_table('governmentleavedates',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyid', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['companyid'], ['companymodel.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_governmentleavedates_id'), 'governmentleavedates', ['id'], unique=False)
    op.create_table('officialholiday',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('companyid', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.ForeignKeyConstraint(['companyid'], ['companymodel.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_officialholiday_id'), 'officialholiday', ['id'], unique=False)
    # op.drop_index('auth_user_groups_group_id_97559544', table_name='auth_user_groups')
    # op.drop_index('auth_user_groups_user_id_6a12ed8b', table_name='auth_user_groups')
    # op.drop_table('auth_user_groups')
    # op.drop_table('author')
    # op.drop_index('ix_user_email', table_name='user')
    # op.drop_index('ix_user_id', table_name='user')
    # op.drop_table('user')
    # op.drop_table('hero')
    # op.drop_index('my_cache_table_expires', table_name='my_cache_table')
    # op.drop_table('my_cache_table')
    # op.drop_table('transactionstate')
    # op.drop_table('recipient')
    # op.drop_table('remitbankdeposit')
    # op.drop_table('django_migrations')
    # op.drop_index('auth_group_permissions_group_id_b120cbf9', table_name='auth_group_permissions')
    # op.drop_index('auth_group_permissions_permission_id_84c5c92e', table_name='auth_group_permissions')
    # op.drop_table('auth_group_permissions')
    # op.drop_table('django_content_type')
    # op.drop_table('banners_banner')
    # op.drop_index('django_session_expire_date_a5c62663', table_name='django_session')
    # op.drop_index('django_session_session_key_c0390e0f_like', table_name='django_session')
    # op.drop_table('django_session')
    # op.drop_table('baseapp_currencyrate')
    # op.drop_index('authtoken_token_key_10f0b77e_like', table_name='authtoken_token')
    # op.drop_table('authtoken_token')
    # op.drop_table('kyc')
    # op.drop_table('remituser')
    # op.drop_index('ix_users_email', table_name='users')
    # op.drop_index('ix_users_id', table_name='users')
    # op.drop_table('users')
    # op.drop_index('ix_book_id', table_name='book')
    # op.drop_table('book')
    # op.drop_table('foreignexchangecharge')
    # op.drop_table('remitdepost')
    # op.drop_table('remitotp')
    # op.drop_table('recivingmethod')
    # op.drop_table('kycstate')
    # op.drop_table('foreignexchange')
    # op.drop_table('transaction')
    # op.drop_index('django_admin_log_content_type_id_c4bce8eb', table_name='django_admin_log')
    # op.drop_index('django_admin_log_user_id_c564eba6', table_name='django_admin_log')
    # op.drop_table('django_admin_log')
    # op.drop_index('auth_group_name_a6ea08ec_like', table_name='auth_group')
    # op.drop_table('auth_group')
    # op.drop_table('userprofile')
    # op.drop_table('cashpickup')
    # op.drop_index('auth_permission_content_type_id_2f476e4b', table_name='auth_permission')
    # op.drop_table('auth_permission')
    # op.drop_table('banners')
    # op.drop_table('baseapp_contact')
    # op.drop_index('auth_user_user_permissions_permission_id_1fbb5f2c', table_name='auth_user_user_permissions')
    # op.drop_index('auth_user_user_permissions_user_id_a95ead1b', table_name='auth_user_user_permissions')
    # op.drop_table('auth_user_user_permissions')
    # op.drop_index('auth_user_username_6821ab7c_like', table_name='auth_user')
    # op.drop_table('auth_user')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('auth_user',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('password', sa.VARCHAR(length=128), autoincrement=False, nullable=False),
    sa.Column('last_login', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('username', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(length=254), autoincrement=False, nullable=False),
    sa.Column('is_staff', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('date_joined', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_user_pkey'),
    sa.UniqueConstraint('username', name='auth_user_username_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('auth_user_username_6821ab7c_like', 'auth_user', ['username'], unique=False)
    op.create_table('auth_user_user_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_user_user_permi_permission_id_1fbb5f2c_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_user_permissions_user_id_a95ead1b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_user_permissions_pkey'),
    sa.UniqueConstraint('user_id', 'permission_id', name='auth_user_user_permissions_user_id_permission_id_14a6b632_uniq')
    )
    op.create_index('auth_user_user_permissions_user_id_a95ead1b', 'auth_user_user_permissions', ['user_id'], unique=False)
    op.create_index('auth_user_user_permissions_permission_id_1fbb5f2c', 'auth_user_user_permissions', ['permission_id'], unique=False)
    op.create_table('baseapp_contact',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('message', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='baseapp_contacts_pkey')
    )
    op.create_table('banners',
    sa.Column('url', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('image', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='banners_pkey')
    )
    op.create_table('auth_permission',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('codename', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='auth_permission_content_type_id_2f476e4b_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_permission_pkey'),
    sa.UniqueConstraint('content_type_id', 'codename', name='auth_permission_content_type_id_codename_01ab375a_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_index('auth_permission_content_type_id_2f476e4b', 'auth_permission', ['content_type_id'], unique=False)
    op.create_table('cashpickup',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='cashpickup_pkey')
    )
    op.create_table('userprofile',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('nationality', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('profile_type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('status_of_residence', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('business_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('business_registered_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('passport_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('referal_code', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('profession', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('residence_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('organization_type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['remituser.id'], name='userprofile_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='userprofile_pkey')
    )
    op.create_table('auth_group',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(length=150), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='auth_group_pkey'),
    sa.UniqueConstraint('name', name='auth_group_name_key'),
    postgresql_ignore_search_path=False
    )
    op.create_index('auth_group_name_a6ea08ec_like', 'auth_group', ['name'], unique=False)
    op.create_table('django_admin_log',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('action_time', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('object_id', sa.TEXT(), autoincrement=False, nullable=True),
    sa.Column('object_repr', sa.VARCHAR(length=200), autoincrement=False, nullable=False),
    sa.Column('action_flag', sa.SMALLINT(), autoincrement=False, nullable=False),
    sa.Column('change_message', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('content_type_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.CheckConstraint('action_flag >= 0', name='django_admin_log_action_flag_check'),
    sa.ForeignKeyConstraint(['content_type_id'], ['django_content_type.id'], name='django_admin_log_content_type_id_c4bce8eb_fk_django_co', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='django_admin_log_user_id_c564eba6_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='django_admin_log_pkey')
    )
    op.create_index('django_admin_log_user_id_c564eba6', 'django_admin_log', ['user_id'], unique=False)
    op.create_index('django_admin_log_content_type_id_c4bce8eb', 'django_admin_log', ['content_type_id'], unique=False)
    op.create_table('transaction',
    sa.Column('sender_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('recipient_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('payment_mode', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('reciving_method', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('closed_exchange_rate', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('amount_deposited', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('source_of_fund', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('service_charge', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('purpose', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('deposit_method', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('remarks', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('date_of_transfer', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('status', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['recipient_id'], ['recipient.id'], name='transaction_recipient_id_fkey'),
    sa.ForeignKeyConstraint(['reciving_method'], ['recivingmethod.id'], name='transaction_reciving_method_fkey'),
    sa.ForeignKeyConstraint(['sender_id'], ['remituser.id'], name='transaction_sender_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='transaction_pkey')
    )
    op.create_table('foreignexchange',
    sa.Column('min_amount', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('is_flat', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('charge_upto_one_lakh', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('carge_from_one_ten_lakh', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('charge_from_ten_lakh_to_1core', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('charge_upto_one_lakh_in_percentage', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('charge_from_one_ten_lakh_in_percentage', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('charge_from_ten_lakh_to_1core_in_percentage', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('created_at', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('cancellation_charge', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='foreignexchange_pkey')
    )
    op.create_table('kycstate',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('front_img', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('back_img', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('tilted_img', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('selfie_img', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('state', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('dob', sa.DATE(), autoincrement=False, nullable=True),
    sa.Column('nationality', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('intended_use_of_account', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('mobile_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('date_of_issue', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('peroid_of_stay', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('expire_date', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('postal', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('prefecture', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('street_address', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('building_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('expiry_date', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('annual_income', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('source_of_income', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('tax_return', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('home_contact_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('emergency_contact_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['remituser.id'], name='kycstate_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='kycstate_pkey')
    )
    op.create_table('recivingmethod',
    sa.Column('recipient_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('payment_mode', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('account_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('pickup_address', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['recipient_id'], ['recipient.id'], name='recivingmethod_recipient_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='recivingmethod_pkey')
    )
    op.create_table('remitotp',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('otp_code', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phoneOrEmail', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('created_at', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('updated_at', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='remitotp_pkey')
    )
    op.create_table('remitdepost',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('location', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('mobile', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('logo', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('country', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='remitdepost_pkey')
    )
    op.create_table('foreignexchangecharge',
    sa.Column('min_amount', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('is_flat', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('charge_upto_one_lakh', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('carge_from_one_ten_lakh', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('charge_from_ten_lakh_to_1core', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('charge_upto_one_lakh_in_percentage', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('charge_from_one_ten_lakh_in_percentage', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('charge_from_ten_lakh_to_1core_in_percentage', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('created_at', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('updated_at', postgresql.TIMESTAMP(), autoincrement=False, nullable=False),
    sa.Column('cancellation_charge', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('issuance_charge', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='foreignexchangecharge_pkey')
    )
    op.create_table('book',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('rating', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=True),
    sa.Column('time_created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('time_updated', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('author_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.ForeignKeyConstraint(['author_id'], ['author.id'], name='book_author_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='book_pkey')
    )
    op.create_index('ix_book_id', 'book', ['id'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('verified', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='users_pkey')
    )
    op.create_index('ix_users_id', 'users', ['id'], unique=False)
    op.create_index('ix_users_email', 'users', ['email'], unique=False)
    op.create_table('remituser',
    sa.Column('phone', sa.VARCHAR(length=16), autoincrement=False, nullable=True),
    sa.Column('total_limit', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('per_day_limit', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('per_month_limit', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('per_year_limit', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('per_day_amount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('per_month_amount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('per_year_amount', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('username', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('photo', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone_verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('verified', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('kyc_status', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('kyc_verified', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('is_staff', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('role', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), server_default=sa.text("nextval('remituser_id_seq'::regclass)"), autoincrement=True, nullable=False),
    sa.Column('fcm_token', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('refrence_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='remituser_pkey'),
    postgresql_ignore_search_path=False
    )
    op.create_table('kyc',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('front_img', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('back_img', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('tilted_img', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('selfie_img', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('user_title', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('dob', sa.DATE(), autoincrement=False, nullable=False),
    sa.Column('nationality', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('intended_use_of_account', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('mobile_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone_number', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('gender', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('date_of_issue', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('peroid_of_stay', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('expire_date', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('postal', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('prefecture', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('city', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('street_address', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('building_name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('expiry_date', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('annual_income', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('source_of_income', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('tax_return', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('home_contact_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('emergency_contact_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['remituser.id'], name='kyc_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='kyc_pkey')
    )
    op.create_table('authtoken_token',
    sa.Column('key', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('created', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='authtoken_token_user_id_35299eff_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('key', name='authtoken_token_pkey'),
    sa.UniqueConstraint('user_id', name='authtoken_token_user_id_key')
    )
    op.create_index('authtoken_token_key_10f0b77e_like', 'authtoken_token', ['key'], unique=False)
    op.create_table('baseapp_currencyrate',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('created_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('updated_at', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.Column('iso3', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=50), autoincrement=False, nullable=False),
    sa.Column('unit', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('buy', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.Column('sell', postgresql.DOUBLE_PRECISION(precision=53), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='baseapp_currencyrate_pkey')
    )
    op.create_table('django_session',
    sa.Column('session_key', sa.VARCHAR(length=40), autoincrement=False, nullable=False),
    sa.Column('session_data', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('expire_date', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('session_key', name='django_session_pkey')
    )
    op.create_index('django_session_session_key_c0390e0f_like', 'django_session', ['session_key'], unique=False)
    op.create_index('django_session_expire_date_a5c62663', 'django_session', ['expire_date'], unique=False)
    op.create_table('banners_banner',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('logo', sa.VARCHAR(length=100), autoincrement=False, nullable=True),
    sa.Column('url', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(length=256), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='banners_banner_pkey')
    )
    op.create_table('django_content_type',
    sa.Column('id', sa.INTEGER(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=2147483647, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app_label', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.Column('model', sa.VARCHAR(length=100), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_content_type_pkey'),
    sa.UniqueConstraint('app_label', 'model', name='django_content_type_app_label_model_76bd3d3b_uniq'),
    postgresql_ignore_search_path=False
    )
    op.create_table('auth_group_permissions',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('permission_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_group_permissions_group_id_b120cbf9_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['permission_id'], ['auth_permission.id'], name='auth_group_permissio_permission_id_84c5c92e_fk_auth_perm', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_group_permissions_pkey'),
    sa.UniqueConstraint('group_id', 'permission_id', name='auth_group_permissions_group_id_permission_id_0cd325b0_uniq')
    )
    op.create_index('auth_group_permissions_permission_id_84c5c92e', 'auth_group_permissions', ['permission_id'], unique=False)
    op.create_index('auth_group_permissions_group_id_b120cbf9', 'auth_group_permissions', ['group_id'], unique=False)
    op.create_table('django_migrations',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('app', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('name', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('applied', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('id', name='django_migrations_pkey')
    )
    op.create_table('remitbankdeposit',
    sa.Column('bank_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('logo', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('account_holder_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('account_number', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('phone', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='remitbankdeposit_pkey')
    )
    op.create_table('recipient',
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('recipient_type', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('recipient_country', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('currency', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('relationship', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('title', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('first_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('last_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('email', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('mobile', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('address', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('note', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('is_quick_send', sa.BOOLEAN(), autoincrement=False, nullable=False),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.ForeignKeyConstraint(['user_id'], ['remituser.id'], name='recipient_user_id_fkey'),
    sa.PrimaryKeyConstraint('id', name='recipient_pkey')
    )
    op.create_table('transactionstate',
    sa.Column('recipient_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('reciving_method', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('recipient_method_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('purpose', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('deposit_method', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('deposit_id', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('deposit_date', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('amount', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='transactionstate_pkey')
    )
    op.create_table('my_cache_table',
    sa.Column('cache_key', sa.VARCHAR(length=255), autoincrement=False, nullable=False),
    sa.Column('value', sa.TEXT(), autoincrement=False, nullable=False),
    sa.Column('expires', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=False),
    sa.PrimaryKeyConstraint('cache_key', name='my_cache_table_pkey')
    )
    op.create_index('my_cache_table_expires', 'my_cache_table', ['expires'], unique=False)
    op.create_table('hero',
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('secret_name', sa.VARCHAR(), autoincrement=False, nullable=False),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.PrimaryKeyConstraint('id', name='hero_pkey')
    )
    op.create_table('user',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('email', sa.VARCHAR(length=60), autoincrement=False, nullable=False),
    sa.Column('hashed_password', sa.VARCHAR(length=256), autoincrement=False, nullable=False),
    sa.Column('is_active', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.Column('is_superuser', sa.BOOLEAN(), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='user_pkey')
    )
    op.create_index('ix_user_id', 'user', ['id'], unique=False)
    op.create_index('ix_user_email', 'user', ['email'], unique=False)
    op.create_table('author',
    sa.Column('id', sa.INTEGER(), autoincrement=True, nullable=False),
    sa.Column('name', sa.VARCHAR(), autoincrement=False, nullable=True),
    sa.Column('age', sa.INTEGER(), autoincrement=False, nullable=True),
    sa.Column('time_created', postgresql.TIMESTAMP(timezone=True), server_default=sa.text('now()'), autoincrement=False, nullable=True),
    sa.Column('time_updated', postgresql.TIMESTAMP(timezone=True), autoincrement=False, nullable=True),
    sa.PrimaryKeyConstraint('id', name='author_pkey')
    )
    op.create_table('auth_user_groups',
    sa.Column('id', sa.BIGINT(), sa.Identity(always=False, start=1, increment=1, minvalue=1, maxvalue=9223372036854775807, cycle=False, cache=1), autoincrement=True, nullable=False),
    sa.Column('user_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.Column('group_id', sa.INTEGER(), autoincrement=False, nullable=False),
    sa.ForeignKeyConstraint(['group_id'], ['auth_group.id'], name='auth_user_groups_group_id_97559544_fk_auth_group_id', initially='DEFERRED', deferrable=True),
    sa.ForeignKeyConstraint(['user_id'], ['auth_user.id'], name='auth_user_groups_user_id_6a12ed8b_fk_auth_user_id', initially='DEFERRED', deferrable=True),
    sa.PrimaryKeyConstraint('id', name='auth_user_groups_pkey'),
    sa.UniqueConstraint('user_id', 'group_id', name='auth_user_groups_user_id_group_id_94350c0c_uniq')
    )
    op.create_index('auth_user_groups_user_id_6a12ed8b', 'auth_user_groups', ['user_id'], unique=False)
    op.create_index('auth_user_groups_group_id_97559544', 'auth_user_groups', ['group_id'], unique=False)
    op.drop_index(op.f('ix_officialholiday_id'), table_name='officialholiday')
    op.drop_table('officialholiday')
    op.drop_index(op.f('ix_governmentleavedates_id'), table_name='governmentleavedates')
    op.drop_table('governmentleavedates')
    op.drop_index(op.f('ix_businessleavedays_id'), table_name='businessleavedays')
    op.drop_table('businessleavedays')
    # ### end Alembic commands ###
