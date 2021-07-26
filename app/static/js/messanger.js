'use strict';
const e = React.createElement;

function App() {
    const [list, setList] = React.useState([]);
    const [count, setCount] = React.useState(0);
    const [pages, setPages] = React.useState([]);
    const [page, setPage] = React.useState(0);
    const [showModal, setShowModal] = React.useState(false);

    const success = (data) => {
        setList(data.data);
        setCount(data.count);
        const newPages = [];
        if (data.count > 10) {
          for (let i=0; i<Math.ceil(data.count / 10); i++) {
            newPages.push({
              name: (i+1).toString(),
              page: i,
            });
            console.log("page",i);
          }
          if (page > newPages.length-1) {
            setPage(page-1);
          }
        } else {
          setPage(0);
        }
        setPages(newPages);
    };

    const logout = async (e)=>{
        await localStorage.setItem("salesToken",null);
        window.location = "/login";
    };

    const getData = ()=>{
        get_orders_api(page, success, (text)=>{console.log("Error: ", text)});
    };

    const keyDownHandler = (e)=>{
        if (e.which === 27)
          setShowModal(false);
    };
  
    React.useEffect(()=>{
        getData();
    }, [page]);

    return (
        <div onKeyDown={keyDownHandler}>
            <div style={{maxWidth: "800px", margin: "auto", marginTop: "1em", marginBottom: "1em",
                          padding: "1em"}} className="shadow">
                <div style={{display: "flex", flexDirection: "row"}}>
                  <span>Alert Messenger App</span>
                  <a className="btn btn-light" style={{marginLeft: "auto"}} onClick={logout}>Logout</a>
                </div>
            </div>
          <div style={{maxWidth: "800px", margin: "auto", marginTop: "1em", marginBottom: "1em",
                        padding: "1em"}} className="shadow">
            
            { list.map((row)=>
              <div class={row.alert_color} role="alert">
                {/* <span class="closebtn" onclick="this.parentElement.style.display='none';">&times;</span>  */}
                <strong>{row.alert_msg}</strong>
                <br/>
              </div>
            )}
          </div>
        </div>
    );
}

const domContainer = document.querySelector('#reactAppContainer');
ReactDOM.render(
  e(App),
  domContainer
);