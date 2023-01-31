## commands
`Ctrl + Shift + P to add Lorem ips paragraf`

```css

```
`here highlighted`
- first
- second


| first  | second |
| :----- | :----- |
| answer | answer |
| answer | answer |
| answer | answer |

-------
## first include the bootstrap links for java and css
```html
<link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-GLhlTQ8iRABdZLl6O3oVMWSktQOp6b7In1Zl3/Jr59b6EGGoI1aFkw7cmDA6j6gD" crossorigin="anonymous">

```
```html
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.0-alpha1/dist/js/bootstrap.bundle.min.js" integrity="sha384-w76AqPfDkMBDXo30jS1Sgez6pr3x5MlQ1ZAGC+nuZB+EYdgRZgiwxhTBTkF7CXvN" crossorigin="anonymous"></script>

```
# add to your vscode the extension
- HTML CSS Support
  
----
## boot strap use 3 layers
- container ass div
- row as div 
- collomns 
```html
<div class="container"> </div>
<div class="container-md"> </div>
<div class="container-lg"> </div>
<div class="container-sm"> </div>
<div class="container-xl"> </div>
<div class="container-xxl"> </div>
<div class="container-fluid"> full size</div>
```
# box system
the bootstrap row contain based on `12 flex boxes`
and it fill her self automatically with max amount 
we have.

```HTML
<div class="row row-cols-4 row-cols-xl-6 gy-2 gy-xl-3 g-s-1">
    <div class="col-6 offset-3">
        <div class="box">box1</div>
        <div class="box">box2</div>
    </div>
    <div class="col-auto">
        <div class="box">box1</div>
        <div class="box">box2</div>
    </div>
    <div class="col-lg-3 col-xxl-4 col-6">
        <div class="box">box1</div>
        <div class="box">box2</div>
    </div>
</div>

```
# Tables
```HTML
<div class="container">
<table class="table">
    <thead>
        <tr>
            <td>Frist</td>
            <td>Second</td>
            <td>Therd</td>
        </tr>
    </thead>
    <tbody>
        <tr>
            <td>Abd</td>
            <td>M</td>
            <td>22</td>
            </tr>
        <tr>
            <td>Kamar</td>
            <td>F</td>
            <td>9</td>
            </tr>
        <tr>
            <td>Adam</td>
            <td>M</td>
            <td>1</td>
            </tr>
    </tbody>
</table>    
</div>
```
# Table colors
- table-active
- table-danger
- table-dark
- table-info
- table-light
- table-primary
- table-secondary
- table-success
  
# Table attribute
## class :
```HTML
class="table table-striped"
class="table table-striped-columns"
class="table table-striped-hover"
class="table table-border"
class="table table-borderless"
class="table "
```
# table responsiv
with table-responsive we remove overflow wen we habe big table.
```HTML
<div class="container">
    <div class="table-responsive">
        <table class="table">
            <thead>
                <tr>
                    <td>Frist</td>
                    <td>Second</td>
                    <td>Therd</td>
                </tr>
            </thead>
            <tbody>
                <tr>
                    <td>Abd</td>
                    <td>M</td>
                    <td>22</td>
                    </tr>
                <tr>
                    <td>Kamar</td>
                    <td>F</td>
                    <td>9</td>
                    </tr>
                <tr>
                    <td>Adam</td>
                    <td>M</td>
                    <td>1</td>
                    </tr>
            </tbody>
        </table>   
    </div> 
</div>
```
# table-group-devider
make a black line to separate the head or body or foot of a table.
```HTML
<thead class="table-group-devider">
<tbody class="table-group-devider">
<tfoot class="table-group-devider">
```
# Forms
```HTML
<div class="container">
    <form>
        <label for="email" class="form-label">Email</label>
        <input type="email" id="email" class="form-control">
        <button>Submit</button>
    </form>
</div>
```
# Form attribute
- form-control-sm
- form-control-lg
#
```HTML
<div class="container">
    <form>
        <label for="email" class="form-label">Email</label>
        <input type="color"  class="form-control form-control-color">
        <button>Submit</button>
    </form>
</div>
```
#
```HTML
<div class="container">
    <form>
        <label for="email" class="form-label">Email</label>
        <input type="range"  class="form-range">
        <button>Submit</button>
    </form>
</div>
```
# Form checkbox 
do not forget to add div with class form-check.
```HTML
<div class="container">
    <form>
        <div class="form-check form-switch form-check-inline">
            <label for="email" class="form-check-label">Email</label>
            <input type="checkbox" class="form-check-input">
            <button>Submit</button>
        </div>
        <div class="form-check form-switch form-check-inline">
            <label for="email" class="form-check-label">Email</label>
            <input type="checkbox" class="form-check-input">
            <button>Submit</button>
        </div>
    </form>
</div>
```
we add form-check-inline to make the checkboxes inline wen we have multeble check boxes.
#
```HTML
<div class="container">
    <form>
        <label for="email" class="form-label">Email</label>
        <select class="form-select form-select-sm">
            <option>1</option>
            <option>2</option>
            <option>3</option>
        </select>
        <button>Submit</button>
    </form>
</div>
```
# Input-group

```HTML
<div class="container">
    <form>
        <label for="text" class="form-label">Amount</label>
        <div class="imput-group">
            <div class="input-group-text">$</div>
            <input type="number" id="text" class="form-control">
            <button class="btn btn-primary">add</button>
        </div>
        <button>Submit</button>
    </form>
</div>
```
# time 31:00 
[video](https://www.youtube.com/watch?v=Jyvffr3aCp0)
#
# floating label
we have to right the input then the label then we have the floating label inside the input.
```HTML

<div class="container">
    <form>
        <div class="form-floating">
            <input type="number" id="text" class="form-control" placeholder="screen reader info here">
            <label for="text" class="form-label">Amount</label>
        </div>
        <button>Submit</button>
    </form>
</div>
```
# form validation
we use `novalidate` in the form tag to disable the validation in html and add the validation in javascript.

```HTML

<div class="container">
    <form novalidate>
        <label for="text" class="form-label">Amount</label>
        <input type="number" id="text" class="form-control" placeholder="screen reader info here">
        <div class="invalid-feedback">invalid-feedback</div>
        <div class="valid-feedback">valid-feedback</div>
        <button>Submit</button>
    </form>
</div>
<script>
    form.addEventListener("submit",e =>{
        if (!form.checkValidity()){
            e.preventDefault()
        }
        form.classList.add("was-validated")
    })
</script>
```
# Button component
- btn-sm
- btn-lg
- btn-outline-secondary
- btn-primary  disabled
- btn-outline-primary
- add attribute --> data-bs-toggle="button" make it line switsch
- we cann make  the button active by add class `active` and the attribute aria-pressed="true" for the screen reader.
- we cann make `btn-group` by add div with class btn-group and but all the buttons inside this div
```HTML
<div class="container">
    <div class="btn-group btn-group-lg btn-group-vertical">
        <button class="btn btn-primary">Test</button>
        <button class="btn btn-primary">Test</button>
        <a class="btn btn-primary" href="#">Test</a>
    </div>
</div>
```

# Alert with button to close with toggle effect
```HTML
<div class="container">
    <div class="alert alert-success alert-dismissible fade show" role="alert">
        <h1>Alert</h1>
        <a href="#" class="alert-link">Go here for mor info<a>
        <button class="btn-close" aria-label="close" data-bs-dismiss="alert"></button>
    </div>
</div>
```
# Card in bootstrap
- card container with class `card`
- card-header
- card-body
- card-title
- card-subtitle
- card-text
- card-img-top
- card-img-bottom
- card-footer
- card-group

```HTML
<div class="container">
    <div class="card">
        <img class="card-img-top" src="#">
        <div class="card-body">
            <h2 class="card-titel">title</h2>
            <p class="card-subtitle">subtitle</p>
            <p class="card-text">Nostrud consequat Lorem duis veniam proident sint enim sunt irure est aliqua. Duis exercitation minim nostrud ea elit adipisicing eiusmod commodo. Non magna anim reprehenderit ut ad non non. Magna incididunt veniam nisi culpa aliqua culpa adipisicing velit.</p>
        </div>
    </div>
</div>
```

# card-img-overlay
we but the img in the background of the card 
```HTML
<div class="container">
    <div class="card">
        <img class="card-img" src="#">
        <div class="card-body card-img-overlay">
            <h2 class="card-titel">title</h2>
            <p class="card-subtitle">subtitle</p>
            <p class="card-text">Nostrud consequat Lorem duis veniam proident sint enim sunt irure est aliqua. Duis exercitation minim nostrud ea elit adipisicing eiusmod commodo. Non magna anim reprehenderit ut ad non non. Magna incididunt veniam nisi culpa aliqua culpa adipisicing velit.</p>

        </div>
    </div>
</div>
```
# modals

# collapse card or box
- data-bs-target="#row"  `we select the target we control`
- aria-expanded="false" `is the target closed or opened`
- data-bs-toggle="collapse"  `what type of action we do`
- aria-controls="row" `what type of thing we control`
- we cann toggle mor then one box at same time with `data-bs-target="row"` use `class` not `id` in css.
```HTML
<div class="container">
    <button class="btn btn-primary" data-bs-toggle="collapse" data-bs-target="#row" aria-expanded="false" aria-controls="row">Toggle</button>
    <div class="row collapse" id="row">
        <div class="box"><div>
    </div>
</div>

```
# navbar
```HTML
<nav class="navbar navbar-expand navbar-dark bg-dark">
    <div class="container">
        <a href="#" class="navbar-brand">Brand</a>
        <ul class="navbar-nav">
            <li class="navbar-item">
                <a href="#" class="nav-link active" aria-current="Home">Home</a>
            </li>
            <li class="navbar-item">
                <a href="#" class="nav-link">Store</a>
            </li>
        </ul>
    </div>
</nav>
```
# navbar collapse
```HTML
<nav class="navbar navbar-expand-md navbar-dark bg-dark">
    <div class="container">
        <a href="#" class="navbar-brand">Brand</a>
        <button class="navbar-toggler" data-bs-toggle="collapse" data-bs-target="#nav" aria-label="Expand Navigation">
            <div class="navbar-toggler-icon"></div>
        </button>
        <div class="collapse navbar-collapse" id="nav">
            <ul class="navbar-nav">
                <li class="navbar-item">
                    <a href="#" class="nav-link active" aria-current="Home">Home</a>
                </li>
                <li class="navbar-item">
                    <a href="#" class="nav-link">Store</a>
                </li>
            </ul>
        </div>
    </div>
</nav>
```
# Color utilities
- bg-white text-light
- text-bg-dark
-  bg-opacity-25
-  text-opacity-25
-  link-danger
-  link-dark
-  opacity-30
-  vstack   vertical stack
-  hstack  
-  border-primary
-  border-3 or 4 or any
-  border add class border to sumthing
-  rounded
-  rounded-3
-  rounded-circle
-  rounded-pill
-  rounded-top
-  rounded-bottom
-  border-top
-  border-start
-  border-opacity-25
-  display --> d-flex
-  d-non
-  d-lg-none
-  d-block
-  padding --> p-4
-  pt-5   top
-  ps-1
-  pe-1
-  pb-1
-  m-lg-5 `Margin`
-  m-auto
-  p-auto

# flexbox utilities
- d-flex 
- justify-content-around
- justify-content-start
- justify-content-center
- justify-content-end
- justify-content-between
- align-items-center
- align-items-stretch
- flex-wrap
- flex-nowrap
- flex-column
- 

```HTML
<div class="container">
    <div class="d-flex justify-content-start ">
        <div class="box" style="width:100px;"></div>
        <div class="box" style="width:100px;"></div>
        <div class="box" style="width:100px;"></div>
        <div class="box" style="width:100px;"></div>
    </div>

</div>
```
[css in 20 minutes](https://www.youtube.com/watch?v=1PnVor36_40)