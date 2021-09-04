const fadeIns = document.querySelectorAll('.fade-in');
const sliders = document.querySelectorAll('.slide-in')

const options = {
    root: null,
    threshold: 0,
    rootMargin: "-150px"
}

const sectionObserver = new IntersectionObserver((entries, sectionObserver) =>{
    entries.forEach(entry =>{
        if(entry.isIntersecting){
            entry.target.classList.add('appear')
            sectionObserver.unobserve(entry.target)
        }
        else{return}
    })
},options)

fadeIns.forEach(fadeIn =>{
    sectionObserver.observe(fadeIn)
})

sliders.forEach(slider =>{
    sectionObserver.observe(slider)
})