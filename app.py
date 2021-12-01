from flask import Flask, render_template, redirect
from flask_debugtoolbar import DebugToolbarExtension
from forms import PetForm, EditPetForm
from models import db, connect_db, Pet

app = Flask(__name__)

app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///adoption_agency'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_ECHO'] = True
app.config['SECRET_KEY'] = "shilohiscute"
app.config['DEBUG_TB_INTERCEPT_REDIRECTS'] = False
debug = DebugToolbarExtension(app)

connect_db(app)

@app.route('/')
def show_homepage():
    """links to homepage; shows list of pets"""
    pets = Pet.query.order_by(Pet.age, Pet.name).all()

    return render_template('home.html', pets=pets)

@app.route('/add', methods=['GET', 'POST'])
def show_add_pet_form():
    """displays form for adding new pet"""

    form = PetForm()

    if form.validate_on_submit():
        name = form.name.data
        species = form.species.data
        photo_url = form.photo_url.data
        age = form.age.data
        notes = form.notes.data

        new_pet = Pet(
            name=name, 
            species=species,
            photo_url=photo_url,
            age=age,
            notes=notes)
        db.session.add(new_pet)
        db.session.commit()

        return redirect('/')
    else:
        return render_template('pet-form.html', form=form)

@app.route('/<int:pet_id>')
def show_pet_details(pet_id):
    """shows details about a specific pet"""

    pet = Pet.query.get_or_404(pet_id)

    return render_template('pet-details.html', pet=pet)

@app.route('/<int:pet_id>/edit', methods=['GET', 'POST'])
def show_edit_form(pet_id):
    """displays form to edit a pet"""

    pet = Pet.query.get_or_404(pet_id)
    form = EditPetForm(obj=pet)

    if form.validate_on_submit():
        pet.photo_url = form.photo_url.data
        pet.notes = form.notes.data
        pet.available = form.available.data
        db.session.commit()

        return redirect(f'/{pet_id}')
    else:
        return render_template('pet-edit-form.html', form=form)



    