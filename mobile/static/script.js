const menuBtn = document.getElementById('nav')
        const closeMenuBtn = document.getElementById('closeBtn')
        const sidebarDOM = document.getElementById('menu')
        const navmenu = document.getElementById('nav')
        const menuUl = document.getElementById('menuUl')

        menuBtn.addEventListener('click', () => {
            menu.classList.add('showSidebar')
            navmenu.classList.add('novisible')
        })

        closeMenuBtn.addEventListener('click', () => {
            menu.classList.remove('showSidebar')
            navmenu.classList.remove('novisible')
        })

        menuUl.addEventListener('click', () => {
            menu.classList.remove('showSidebar')
            navmenu.classList.remove('novisible')
        })