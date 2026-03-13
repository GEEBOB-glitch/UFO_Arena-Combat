<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Powerup Demo</title>

<style>
body{
margin:0;
background:black;
display:flex;
justify-content:center;
align-items:center;
height:100vh;
}

canvas{
background:#141432;
border:2px solid cyan;
}
</style>
</head>

<body>

<canvas id="game" width="800" height="500"></canvas>

<script>

const canvas = document.getElementById("game")
const ctx = canvas.getContext("2d")


/* ---------- PLAYER ---------- */

class Player{

constructor(x,y){

this.x=x
this.y=y
this.radius=20

this.invincible=false
this.invincibleEndTime=0

this.rapidFire=false
this.rapidFireEndTime=0

this.score=0
}

update(){

if(this.invincible && Date.now()>this.invincibleEndTime){
this.invincible=false
}

if(this.rapidFire && Date.now()>this.rapidFireEndTime){
this.rapidFire=false
}

}

draw(){

ctx.fillStyle=this.invincible ? "cyan" : "red"

ctx.beginPath()
ctx.arc(this.x,this.y,this.radius,0,Math.PI*2)
ctx.fill()

}

}


/* ---------- POWERUP BASE ---------- */

class Powerup {

constructor(x,y){

this.x=x
this.y=y
this.radius=10

this.lifetime=600
this.collected=false

}

update(){

this.lifetime--

return this.lifetime>0

}

apply(player){}

getColor(){
return "white"
}

draw(ctx){

ctx.fillStyle=this.getColor()

ctx.beginPath()
ctx.arc(this.x,this.y,this.radius,0,Math.PI*2)
ctx.fill()

}

}


/* ---------- SHIELD ---------- */

class ShieldPowerup extends Powerup{

getColor(){
return "rgb(100,200,255)"
}

apply(player){

player.invincible=true
player.invincibleEndTime=Date.now()+8000

}

}


/* ---------- RAPID FIRE ---------- */

class RapidFirePowerup extends Powerup{

getColor(){
return "rgb(255,200,100)"
}

apply(player){

player.rapidFire=true
player.rapidFireEndTime=Date.now()+10000

}

}


/* ---------- SCORE ---------- */

class ScorePowerup extends Powerup{

getColor(){
return "rgb(255,255,100)"
}

apply(player){

player.score+=100

}

}


/* ---------- GAME ---------- */

let player=new Player(400,250)

let powerups=[]


/* spawn random powerup */

function spawnPowerup(){

let x=Math.random()*760+20
let y=Math.random()*460+20

let types=[ShieldPowerup,RapidFirePowerup,ScorePowerup]

let Type=types[Math.floor(Math.random()*types.length)]

powerups.push(new Type(x,y))

}


/* collision */

function checkCollision(a,b){

let dx=a.x-b.x
let dy=a.y-b.y

let dist=Math.sqrt(dx*dx+dy*dy)

return dist < a.radius + b.radius

}


/* input */

const keys={}

window.addEventListener("keydown",e=>{
keys[e.key]=true
})

window.addEventListener("keyup",e=>{
keys[e.key]=false
})


/* update */

function update(){

/* movement */

if(keys["a"]) player.x-=4
if(keys["d"]) player.x+=4
if(keys["w"]) player.y-=4
if(keys["s"]) player.y+=4

player.update()

/* spawn */

if(Math.random()<0.01){
spawnPowerup()
}

/* update powerups */

powerups=powerups.filter(p=>p.update())

/* collect powerups */

for(let p of powerups){

if(checkCollision(player,p)){

p.apply(player)
p.collected=true

}

}

powerups=powerups.filter(p=>!p.collected)

}


/* draw */

function draw(){

ctx.clearRect(0,0,800,500)

player.draw()

for(let p of powerups){
p.draw(ctx)
}

/* UI */

ctx.fillStyle="white"
ctx.font="20px Arial"
ctx.fillText("Score: "+player.score,10,30)

if(player.invincible)
ctx.fillText("Shield Active",10,60)

if(player.rapidFire)
ctx.fillText("Rapid Fire Active",10,90)

}


/* loop */

function gameLoop(){

update()
draw()

requestAnimationFrame(gameLoop)

}

gameLoop()

</script>

</body>
</html>
