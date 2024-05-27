
$('.close-menu-block svg').click((e)=>{
    console.log("ok")
    $(".nav-menu-block").animate({
       right:-300
    }, 1000, ()=>{})
})
$('.menu-button').click((e)=>{
    $(".nav-menu-block").animate({
       right: 0
    }, 1000, ()=>{})
})