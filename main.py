import os
from flask import Flask, render_template, url_for, redirect, request, jsonify
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import desc
from flask_login import UserMixin, login_user, LoginManager, login_required, logout_user, current_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, IntegerField,validators, TextAreaField, TimeField
from wtforms.validators import InputRequired, Length, ValidationError
from flask_bcrypt import Bcrypt
from datetime import datetime, time

app = Flask(__name__, template_folder='template', static_folder='static')
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///database.db'
app.config['SECRET_KEY'] = 'thisisasecretkey'
db = SQLAlchemy(app)
bcrypt = Bcrypt(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = 'login'

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))

class Tindakan(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    no = db.Column(db.Integer)
    jenis_tindakan = db.Column(db.String(100))
    isi_tindakan = db.Column(db.String(200))

class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), nullable=False, unique=True)
    password = db.Column(db.String(80), nullable=False)

class informasi(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    pengingatObat = db.Column(db.String(500), nullable=False)
    jadwalKontrol = db.Column(db.String(500), nullable=False)
    konsul = db.Column(db.String(500), nullable=False)
    hariKesehatan=db.Column(db.String(500), nullable=False)
    infoTambahan = db.Column(db.String(1000), nullable=False)

class kajiPerawat(db.Model):
    id = db.Column(db.Integer, primary_key=True, autoincrement = True)
    nama = db.Column(db.String(80), nullable=False, unique=True)
    jenisKelamin = db.Column(db.String(10), nullable=False)
    usia = db.Column(db.Integer, nullable=False)
    statusPerkawinan = db.Column(db.String(20), nullable=False)
    agama = db.Column(db.String(80), nullable=False)
    sukuBangsa = db.Column(db.String(30), nullable=False)
    pendidikan = db.Column(db.String(20), nullable=False)
    bahasaYangDigunakan = db.Column(db.String(80), nullable=False)
    pekerjaan = db.Column(db.String(80), nullable=False)
    alamat = db.Column(db.String(80), nullable=False)
    diagnosisMedis = db.Column(db.String(80), nullable=False)
    namaPenanggungJawab = db.Column(db.String(80), nullable=False)
    jenisKelaminPJ = db.Column(db.String(15), nullable=False)
    usiaPJ = db.Column(db.Integer, nullable=False)
    hubunganPasien = db.Column(db.String(30), nullable=False)
    pendidikanPJ = db.Column(db.String(40), nullable=False)
    pekerjaanPJ = db.Column(db.String(30), nullable=False)
    alamatPJ = db.Column(db.String(160), nullable=False)
    riwayatKesahatanDulu = db.Column(db.String(500), nullable=False)
    riwayatKesahatanSekarang = db.Column(db.String(500), nullable=False)
    riwayatKesahatanKeluarga = db.Column(db.String(500), nullable=False)
    waktuTidur = db.Column(db.Time, nullable=False)
    waktuBangun = db.Column(db.Time, nullable=False)
    masalahTidur = db.Column(db.String(500), nullable=False)
    permudahTidur = db.Column(db.String(500), nullable=False)
    permudahBangun = db.Column(db.String(500), nullable=False)
    bab =db.Column(db.String(100), nullable=False)
    bak =db.Column(db.String(100), nullable=False)
    kesulitanBabBak =db.Column(db.String(500), nullable=False)
    upayaMengatasiMasalah =db.Column(db.String(500), nullable=False)
    jumlahJenisMakan =db.Column(db.String(500), nullable=False)
    waktuPemberianMakan =db.Column(db.String(500), nullable=False)
    jumlahJenisMinum =db.Column(db.String(500), nullable=False)
    waktuPemberianMinum =db.Column(db.String(500), nullable=False) 
    pantangan =db.Column(db.String(500), nullable=False)
    masalahMakanMinum =db.Column(db.String(500), nullable=False)
    upayaMengatasiMasalahMakanMinum = db.Column(db.String(500), nullable=False)
    pemeliharaanBadan = db.Column(db.String(500), nullable=False)
    pemeliharaanGigi = db.Column(db.String(500), nullable=False)
    pemeliharaanKuku = db.Column(db.String(500), nullable=False)
    kegiatan = db.Column(db.String(500), nullable=False)
    polaKomunikasi = db.Column(db.String(500), nullable=False)
    orangTerdekat = db.Column(db.String(500), nullable=False)
    rekreasi = db.Column(db.String(500), nullable=False)
    dampakDirawat = db.Column(db.String(500), nullable=False)
    hubunganOrangLain = db.Column(db.String(500), nullable=False)
    keluargaDihubungi = db.Column(db.String(500), nullable=False)
    ketaatanIbadah = db.Column(db.String(500), nullable=False)
    keyakinanSehatSakit = db.Column(db.String(500), nullable=False)
    keyakinanPenyembuhan = db.Column(db.String(500), nullable=False)
    kesanUmum = db.Column(db.String(500), nullable=False)
    tandaVital = db.Column(db.String(500), nullable=False)
    pemeriksaanKepalaLehar = db.Column(db.String(500), nullable=False)
    pemeriksaanMata = db.Column(db.String(500), nullable=False)
    pemeriksaanHidung = db.Column(db.String(500), nullable=False)
    pemeriksaanTelinga = db.Column(db.String(500), nullable=False)
    pemeriksaanMulut = db.Column(db.String(500), nullable=False)
    pemeriksaanThorak = db.Column(db.String(500), nullable=False)
    pemeriksaanAbdomen = db.Column(db.String(500), nullable=False)
    pemerikasaanGenitourinaria = db.Column(db.String(500), nullable=False)
    pemeriksaanMuskuloskeletal = db.Column(db.String(500), nullable=False)
    hasilPemeriksaan = db.Column(db.String(500), nullable=False)
    kesimpulanPemeriksaan = db.Column(db.String(500), nullable=False)
    rencanaTindakLanjut = db.Column(db.String(500), nullable=False)
    penataLaksanaan = db.Column(db.String(500), nullable=False)
    terapi = db.Column(db.String(500), nullable=False)  

class dataDiri(db.Model, UserMixin):
    user_id = db.Column(db.Integer, primary_key = True, autoincrement = True)
    nama = db.Column(db.String(500), nullable=False)
    username = db.Column(db.String(30), db.ForeignKey('user.username'), nullable=False, unique=True)
    noKTP =db.Column(db.Integer,  unique=True)
    noWA = db.Column(db.String(12))
    email = db.Column(db.String(50))

class RegisterForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    
    namaAsli = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Nama"})
    
    noKtp = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "No KTP"})
    
    noWa = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "No Wa"})
    
    emailUser = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Email"})

    submit = SubmitField('Register')

    def validate_username(self, username):
        existing_user_username = User.query.filter_by(
            username=username.data).first()
        if existing_user_username:
            raise ValidationError(
                'That username already exists. Please choose a different one.')

class LoginForm(FlaskForm):
    username = StringField(validators=[
                           InputRequired(), Length(min=4, max=20)], render_kw={"placeholder": "Username"})

    password = PasswordField(validators=[
                             InputRequired(), Length(min=8, max=20)], render_kw={"placeholder": "Password"})
    
    submit = SubmitField('Login')

class formKajian(FlaskForm):
    nama = StringField(validators=[InputRequired()], render_kw={"placeholder": "Nama"})
    jenisKelamin = SelectField(validators=[InputRequired()], choices=[('laki', 'Laki-laki'), ('perempuan', 'Perempuan')], render_kw={"placeholder": "Jenis Kelamin"})
    usia = IntegerField(validators=[ validators.NumberRange(min=1, max=99, message='Usia harus antara 1 dan 99'),InputRequired(message='Usia wajib diisi'),], render_kw={"placeholder": "Usia"})
    statusPerkawinan = SelectField(validators=[InputRequired()], choices=[('Nikah', 'Menikah'), ('Belum Nikah', 'Belum Menikah'),('Cerai Hidup', 'Cerai Hidup'), ('Cerai Mati', 'Cerai Mati')],  render_kw={"placeholder": "Status Perkawinan"})
    agama = StringField(validators=[InputRequired()], render_kw={"placeholder": "Agama"})
    sukuBangsa = StringField(validators=[InputRequired()], render_kw={"placeholder": "Suku Bangsa"})
    pendidikan = StringField(validators=[InputRequired()], render_kw={"placeholder": "Pendidikan"})
    bahasaYangDigunakan = StringField(validators=[InputRequired()], render_kw={"placeholder": "Bahasa Yang Digunakan"})
    pekerjaan = StringField(validators=[InputRequired()], render_kw={"placeholder": "Pekerjaan"})
    alamat = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Alamat"})
    diagnosisMedis = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Diagnosis Medis"})
    namaPenanggungJawab =  StringField(validators=[InputRequired()], render_kw={"placeholder": "Nama Penanggung Jawab"})
    jenisKelaminPJ = SelectField(validators=[InputRequired()], choices=[('laki', 'Laki-laki'), ('perempuan', 'Perempuan')],  render_kw={"placeholder": "Jenis Kelamin Penanggung Jawab"})
    usiaPJ = IntegerField(validators=[validators.NumberRange(min=1, max=99, message='Usia harus antara 1 dan 99'),InputRequired()], render_kw={"placeholder": "Usia"})
    hubunganPasien = StringField(validators=[InputRequired()], render_kw={"placeholder": "Hubungan Dengan Pasien"})
    pendidikanPJ = StringField(validators=[InputRequired()], render_kw={"placeholder": "Pendidikan Penanggung Jawab"})
    pekerjaanPJ = StringField(validators=[InputRequired()], render_kw={"placeholder": "Pekerjaan Penanggung Jawab"})
    alamatPJ = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Alamat Penanggung Jawab"})
    riwayatKesahatanDulu = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Riwayat Kesehatan Dulu"})
    riwayatKesahatanSekarang = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Riwayat Kesehatan Sekarang"})
    riwayatKesahatanKeluarga = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Riwayat Kesehatan Keluarga"})
    waktuTidur = TimeField(validators=[InputRequired()], render_kw={"placeholder": "Jam Tidur"})
    waktuBangun = TimeField(validators=[InputRequired()], render_kw={"placeholder": "Jam Bangun"})
    masalahTidur = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Masalah Tidur"})
    permudahTidur = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Permudah Tidur"})
    permudahBangun = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Permudah Bangun"})
    bab = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Aktivitas BAB"})
    bak = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Aktivitas BAK"})
    kesulitanBabBak = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Kendala BAB dan BAK"})
    upayaMengatasiMasalah =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Upaya Mengatasi Masalah"})
    jumlahJenisMakan = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Jumlah Jenis minum"})
    waktuPemberianMakan =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Waktu pemberian makan"})
    jumlahJenisMinum = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Jumlah Jenis minum"})
    waktuPemberianMinum = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Waktu pemberian minum"})
    pantangan = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pantangan"})
    masalahMakanMinum = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Masalah Makan dan Minum"})
    upayaMengatasiMasalahMakanMinum = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Upaya Mengatasinya"})
    pemeliharaanBadan = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pemeliharaan Badan"})
    pemeliharaanGigi = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pemeliharaan Gigi"})
    pemeliharaanKuku = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pemeliharaan Kuku"})
    kegiatan = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Kegiatan"})
    polaKomunikasi = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pola Komunikasi"})
    orangTerdekat = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Orang Dekat Dengan Pasien"})
    rekreasi =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Rekreasi"})
    dampakDirawat = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Dampak Dirawat"})
    hubunganOrangLain = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Hubungan Orang Lain"})
    keluargaDihubungi  = StringField(validators=[InputRequired()], render_kw={"placeholder": "Keluarga yang bisa dihubungi"})
    ketaatanIbadah = StringField(validators=[InputRequired()], render_kw={"placeholder": "Ketaatan Ibadah"})
    keyakinanSehatSakit =StringField(validators=[InputRequired()], render_kw={"placeholder": "Keyakinan Sehat/Sakit"})
    keyakinanPenyembuhan = StringField(validators=[InputRequired()], render_kw={"placeholder": " Keyakinan Sembuh"})
    kesanUmum =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Kesan Umum"})
    tandaVital =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Tanda Vital"})
    pemeriksaanKepalaLehar =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": " Pemeriksaan Kepala Leher"})
    pemeriksaanMata =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pemeriksaan Mata"})
    pemeriksaanHidung =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pemeriksaan Hidung "})
    pemeriksaanTelinga =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pemeriksaan Telinga"})
    pemeriksaanMulut = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pemeriksaan Mulut"})
    pemeriksaanThorak = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pemeriksaan Thorak"})
    pemeriksaanAbdomen =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pemeriksaan Abdomen"})
    pemerikasaanGenitourinaria = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pemeriksaan Genitourinaria"})
    pemeriksaanMuskuloskeletal =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pemeriksaan Muskuloskeletal"})   
    hasilPemeriksaan = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Hasil Pemeriksaan"})
    kesimpulanPemeriksaan =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Kesimpulan Pemeriksaan"})
    rencanaTindakLanjut =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Rencana Tindak Lanjuti"})
    penataLaksanaan =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Penata Laksanaan"})
    terapi =TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Terapi"})
    submit = SubmitField('Kirim')

class infoForm(FlaskForm):
    pengingatObat2 = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Pengingat Obat"})
    jadwalKontrol2 = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Jadwal Kontrol"})
    konsul2 = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Konsultasi"})
    hariKesehatan2= TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Hari Konsultasi"})
    infoTambahan2 = TextAreaField(validators=[InputRequired()], render_kw={"placeholder": "Informasi Tambahan"})
    submit = SubmitField('submit')

@app.route('/informasiTambahan', methods =['GET', 'POST'])
@login_required
def informasiTambahan():
    Form = infoForm()
    if request.method == 'POST'and Form.validate_on_submit():
        print(request.method)
        newInfo = informasi(
                pengingatObat = Form.pengingatObat2.data,
                jadwalKontrol = Form.jadwalKontrol2.data,
                konsul = Form.konsul2.data,
                hariKesehatan= Form.hariKesehatan2.data, 
                infoTambahan = Form.infoTambahan2.data
            )
        db.session.add(newInfo)
        db.session.commit()
    else:
        print(Form.errors)
    data = informasi.query.order_by(informasi.id.desc()).first()
    return render_template('informasi.html', form=Form, Data=data) 

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/sdki')
@login_required
def sdki():
    return render_template('sdki.html')

@app.route('/siki')
@login_required
def siki():
    return render_template('siki.html')

@app.route('/kajianPerawat', methods=['GET','POST'])
@login_required
def kajianPerawat():
    formulir = formKajian()
    if request.method == 'POST' and formulir.validate():
        print(request.method)
        try:
                print(formulir)
                new_kaji = kajiPerawat( 
                nama=formulir.nama.data,
                jenisKelamin=formulir.jenisKelamin.data,
                usia=formulir.usia.data,
                statusPerkawinan=formulir.statusPerkawinan.data,
                agama=formulir.agama.data,
                sukuBangsa=formulir.sukuBangsa.data,
                pendidikan=formulir.pendidikan.data,
                bahasaYangDigunakan=formulir.bahasaYangDigunakan.data,
                pekerjaan=formulir.pekerjaan.data,
                alamat=formulir.alamat.data,
                diagnosisMedis=formulir.diagnosisMedis.data,
                namaPenanggungJawab=formulir.namaPenanggungJawab.data,
                jenisKelaminPJ=formulir.jenisKelaminPJ.data,
                usiaPJ=formulir.usiaPJ.data,
                hubunganPasien=formulir.hubunganPasien.data,
                pendidikanPJ=formulir.pendidikanPJ.data,
                pekerjaanPJ=formulir.pekerjaanPJ.data,
                alamatPJ=formulir.alamatPJ.data,
                riwayatKesahatanDulu=formulir.riwayatKesahatanDulu.data,
                riwayatKesahatanSekarang=formulir.riwayatKesahatanSekarang.data,
                riwayatKesahatanKeluarga=formulir.riwayatKesahatanKeluarga.data,
                waktuTidur=formulir.waktuTidur.data,
                waktuBangun=formulir.waktuBangun.data,
                masalahTidur=formulir.masalahTidur.data,
                permudahTidur=formulir.permudahTidur.data,
                permudahBangun=formulir.permudahBangun.data,
                bab=formulir.bab.data,
                bak=formulir.bak.data,
                kesulitanBabBak=formulir.kesulitanBabBak.data,
                upayaMengatasiMasalah=formulir.upayaMengatasiMasalah.data,
                jumlahJenisMakan=formulir.jumlahJenisMakan.data,
                waktuPemberianMakan=formulir.waktuPemberianMakan.data,
                jumlahJenisMinum=formulir.jumlahJenisMinum.data,
                waktuPemberianMinum=formulir.waktuPemberianMinum.data,
                pantangan=formulir.pantangan.data,
                masalahMakanMinum=formulir.masalahMakanMinum.data,
                upayaMengatasiMasalahMakanMinum=formulir.upayaMengatasiMasalahMakanMinum.data,
                pemeliharaanBadan=formulir.pemeliharaanBadan.data,
                pemeliharaanGigi=formulir.pemeliharaanGigi.data,
                pemeliharaanKuku=formulir.pemeliharaanKuku.data,
                kegiatan=formulir.kegiatan.data,
                polaKomunikasi=formulir.polaKomunikasi.data,
                orangTerdekat=formulir.orangTerdekat.data,
                rekreasi=formulir.rekreasi.data,
                dampakDirawat=formulir.dampakDirawat.data,
                hubunganOrangLain=formulir.hubunganOrangLain.data,
                keluargaDihubungi=formulir.keluargaDihubungi.data,
                ketaatanIbadah=formulir.ketaatanIbadah.data,
                keyakinanSehatSakit=formulir.keyakinanSehatSakit.data,
                keyakinanPenyembuhan=formulir.keyakinanPenyembuhan.data,
                kesanUmum=formulir.kesanUmum.data,
                tandaVital=formulir.tandaVital.data,
                pemeriksaanKepalaLehar=formulir.pemeriksaanKepalaLehar.data,
                pemeriksaanMata=formulir.pemeriksaanMata.data,
                pemeriksaanHidung=formulir.pemeriksaanHidung.data,
                pemeriksaanTelinga=formulir.pemeriksaanTelinga.data,
                pemeriksaanMulut=formulir.pemeriksaanMulut.data,
                pemeriksaanThorak=formulir.pemeriksaanThorak.data,
                pemeriksaanAbdomen=formulir.pemeriksaanAbdomen.data,
                pemerikasaanGenitourinaria=formulir.pemerikasaanGenitourinaria.data,
                pemeriksaanMuskuloskeletal=formulir.pemeriksaanMuskuloskeletal.data,
                hasilPemeriksaan=formulir.hasilPemeriksaan.data,
                kesimpulanPemeriksaan=formulir.kesimpulanPemeriksaan.data,
                rencanaTindakLanjut=formulir.rencanaTindakLanjut.data,
                penataLaksanaan=formulir.penataLaksanaan.data,
                terapi=formulir.terapi.data
                )
                db.session.add(new_kaji)
                db.session.commit()
                return redirect(url_for('dashboard'))
        except Exception as e:
                print(f"Error: {e}")
        return "Gagal menyimpan data"

    return render_template('kajianPerawat.html', form=formulir) 

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(username=form.username.data).first()
        if user:
            if bcrypt.check_password_hash(user.password, form.password.data):
                login_user(user)
                return redirect(url_for('dashboard'))
    return render_template('login.html', form=form)

@app.route('/dashboard', methods=['GET', 'POST'])
@login_required
def dashboard():
    return render_template('dashboard.html')

@app.route('/kta')
@login_required
def kta():
    user = current_user
    user_data = dataDiri.query.filter_by(username = user.username).first()
    return render_template('kta.html', user=user, user_data=user_data)

@app.route('/logout', methods=['GET', 'POST'])
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['GET', 'POST'])
def register():
    form = RegisterForm()

    if form.validate_on_submit():
        try :
            hashed_password = bcrypt.generate_password_hash(form.password.data)
            new_user = User(username=form.username.data, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()

            new_data_diri = dataDiri(username = new_user.username, nama = form.namaAsli.data, noKTP = form.noKtp.data, noWA = form.noWa.data, email=form.emailUser.data )
            db.session.add(new_data_diri)
            db.session.commit()
            return redirect(url_for('login'))
        except Exception as e:
            print(f"Error: {str(e)}")
    return render_template('register.html', form=form)

@app.route('/credit')
@login_required
def credit():
    return render_template('credit.html')

@app.route('/intervansi')
def intervansi():
    queries = Tindakan.query.all()
    return render_template('intervansi.html', queries=queries)

@app.route('/add_query', methods=['POST'])
def add_query():
    no = request.form['no']
    jenis_tindakan = request.form['jenis_tindakan']
    isi_tindakan = request.form['isi_tindakan']
    new_query = Tindakan(no=no, jenis_tindakan=jenis_tindakan, isi_tindakan=isi_tindakan)
    db.session.add(new_query)
    db.session.commit()
    return redirect(url_for('intervansi'))

@app.route('/delete_query/<int:query_id>', methods=['POST'])
def delete_query(query_id):
    query_to_delete = Tindakan.query.get_or_404(query_id)
    db.session.delete(query_to_delete)
    db.session.commit()
    return redirect(url_for('evaluasi'))

@app.route('/evaluasi')
def evaluasi():
    queries = Tindakan.query.all()
    return render_template('evaluasi.html', queries=queries)

@app.route('/diagnosa')
@login_required
def diagnosa():
    # Mengambil data kajiPerawat yang terbaru
    dataDiagnosa = kajiPerawat.query.order_by(kajiPerawat.id.desc()).first()
    

    return render_template("diagnosa.html", dataDiagnosa=dataDiagnosa)



@app.route('/profile')
@login_required
def profile():
    user = current_user
    user_data = dataDiri.query.filter_by(username = user.username).first()
    return render_template("profile.html", user = user, user_data=user_data)

if __name__ == "__main__":
    app.run(debug=True)
