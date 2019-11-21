
var app;
app = new Vue({
    el: '#app',
    delimiters: ['[[', ']]'],
    data: {
        current: '',
        class: 0
    },
    mounted: function () {
        this.summary();        
    },
    methods: {
        summary: () =>{
            axios.get('/data').then(
                response => {
                    app.current = response.data.current;
                    app.id = response.data.id;
                    
                }
            );
        },
        next_comment:(clase)=>{
            axios.get(`/classificate/${clase}/${app.id}`).then();
            axios.get('/data').then(
                response => {
                    app.current = response.data.current;
                    app.id = response.data.id;                    
                }
            );
        }
    }
});


