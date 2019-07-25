var cellOne = document.querySelector('#one')
var cellTwo = document.querySelector('#two')
var cellThree = document.querySelector('#three')
var cellFour = document.querySelector('#four')
var cellFive = document.querySelector('#five')
var cellSix = document.querySelector('#six')
var cellSeven = document.querySelector('#seven')
var cellEigth = document.querySelector('#eight')
var cellNine = document.querySelector('#nine')
var restart = document.querySelector('#b')
restart.addEventListener('click',function(){
 cellOne.textContent = ''
 cellTwo.textContent = ''
 cellThree.textContent = ''
 cellFour.textContent = ''
 cellFive.textContent = ''
 cellSix.textContent = ''
 cellSeven.textContent = ''
 cellEigth.textContent = ''
 cellNine.textContent = ''
})
cellOne.addEventListener('click',function()
{
  cellOne.textContent = 'X'
})
cellOne.addEventListener('dblclick',function()
{
  cellOne.textContent = 'O'
})

cellTwo.addEventListener('click',function()
{
  cellTwo.textContent = 'X'
})
cellTwo.addEventListener('dblclick',function()
{
  cellTwo.textContent = 'O'
})
cellThree.addEventListener('click',function()
{
  cellThree.textContent = 'X'
})
cellThree.addEventListener('dblclick',function()
{
  cellThree.textContent = 'O'
})
cellFour.addEventListener('click',function()
{
  cellFour.textContent = 'X'
})
cellFour.addEventListener('dblclick',function()
{
  cellFour.textContent = 'O'
})
cellFive.addEventListener('click',function()
{
  cellFive.textContent = 'X'
})
cellFive.addEventListener('dblclick',function()
{
  cellFive.textContent = 'O'
})
cellSix.addEventListener('click',function()
{
  cellSix.textContent = 'X'
})
cellSix.addEventListener('dblclick',function()
{
  cellSix.textContent = 'O'
})
cellSeven.addEventListener('click',function()
{
  cellSeven.textContent = 'X'
})
cellSeven.addEventListener('dblclick',function()
{
  cellSeven.textContent = 'O'
})
cellEigth.addEventListener('click',function()
{
  cellEigth.textContent = 'X'
})
cellEigth.addEventListener('dblclick',function()
{
  cellEigth.textContent = 'O'
})
cellNine.addEventListener('click',function()
{
  cellNine.textContent = 'X'
})
cellNine.addEventListener('dblclick',function()
{
  cellNine.textContent = 'O'
})
