import React, {Component} from 'react';
import InputBase from '@material-ui/core/InputBase';
import SingleLineGridList from '../messier/messierList';

class Search extends Component {
    // constructor(props) {
    //   super(props)
    // }
    token = null;
    state = {
      query: "",
      messier: [],
      error: null,
      isLoad: false
    };
    onChange = e => {
      const { value } = e.target;
      this.setState({
        query: value
      });
  
      this.search(value);
    };
  
    search = query => {
      const proxyurl = "https://cors-anywhere.herokuapp.com/";
      const url = `https://anh.pythonanywhere.com/api/v2/messier-catalogue/${query}`;
      const token = {};
      this.token = token;
  
      fetch(proxyurl + url)
        .then(results => results.json())
        .then((dt) => {
          if (this.token === token) {
            if (dt.hasOwnProperty("message")) {
              this.setState({ 
                isLoad: true,
                messier : [],
                error : dt.message
              })
            } else {
              if (dt.data instanceof Object) {
                this.setState({ 
                  isLoad: true,
                  messier: [dt.data] 
                });
              } else {
                this.setState({ 
                  isLoad: true,
                  messier: dt.data 
                });
              }
            }
          }
        }, (error) => {
          this.setState({
            isLoad: true,
            error: error.message  
          })
        })
        // .catch((e) => {console.log(e)});
    };

    // getData() {
    //   this.setState({
    //     data: this.state.messier
    //   })
    // }
  
    componentDidMount() {
      this.setState({
        classes: this.props
      });
      this.search("");
      // this.getData();
    }
  
    render() {
      const { classes } = this.props;
      return (
        // <form>
        //   <input
        //     type="text"
        //     className="search-box"
        //     placeholder="Search for..."
        //     onChange={this.onChange}
        //   />
        //   {
        //   this.state.messier &&
        //   // console.log(typeof(this.state.messier)) &&
        //   // console.log(this.state.messier) &&
        //   <SingleLineGridList data={this.state.messier}/>
        //   // this.state.messier.map(mes => (
        //   //   // console.log(mes) &&
        //   //   <ul key={mes.id}>
        //   //     <li>{mes.id}</li>
        //   //   </ul>
        //   // ))
        //   }
        // </form>
        <div>
        <InputBase
          placeholder="Search…"
          // onChange={handleInputSearchOnChange}
          classes={{
            root: classes.color,
            input: classes.inputInput,
          }}
          inputProps={{ 'aria-label': 'search' }}
          onChange={this.onChange}
          />
            
            {/* {
              this.state.messier &&
              <SingleLineGridList data={this.state.messier}/> 
            } */}
          </div>
      );
    }
  }

  export default Search;