const filter = (type) => {

    const news_cards = document.getElementById('news_cards');

    for (child of news_cards.children) {
        child.style.display = child.dataset?.newsType !== type ? 'none' : 'block'
        child.style.display = type === 'reset' ? 'block' : child.style.display
    }
}

const searchFilter = (event) => {
    event.preventDefault();

    // get search value
    const searchvalue = event.target?.children[0]?.value

    // Filter
    const news_cards = document.getElementById('news_cards');

    for (child of news_cards.children) {
        console.log(child.querySelector('.title').querySelector('h3').innerText);
        console.log(child.querySelector('.post-author').innerText)
        console.log('======')
        child.style.display = 'none'
        if (
            child.querySelector('.post-author').innerText.toLowerCase().includes(searchvalue.toLowerCase()) || // filter by author
            child.querySelector('.title').querySelector('h3').innerText.toLowerCase().includes(searchvalue.toLowerCase())   // filter by substring of title
        ) {
            child.style.display = 'block'
        }
    }
}
const searchForm = document.getElementById('search-form');

searchForm.addEventListener('submit', (e) => searchFilter(e))