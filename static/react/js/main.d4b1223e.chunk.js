(this["webpackJsonprecipe-manager"]=this["webpackJsonprecipe-manager"]||[]).push([[0],{46:function(e,t,a){e.exports=a.p+"media/video.9f09eedc.mp4"},52:function(e,t,a){e.exports=a(89)},57:function(e,t,a){},64:function(e,t,a){},65:function(e,t,a){},66:function(e,t,a){},84:function(e,t,a){},85:function(e,t,a){},86:function(e,t,a){},88:function(e,t,a){},89:function(e,t,a){"use strict";a.r(t);var n=a(1),r=a.n(n),c=a(20),s=a.n(c),i=(a(57),a(3)),u=a.n(i),o=a(4),l=a(9),m=a(10),p=a(11),f=a(7),d=a(12),h=a(41),g=a(42),v=a(50),b=a(43),_=a(51),E=a(5),y=function(e){function t(){var e,a;Object(h.a)(this,t);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(a=Object(v.a)(this,(e=Object(b.a)(t)).call.apply(e,[this].concat(r)))).state={},a}return Object(_.a)(t,e),Object(g.a)(t,[{key:"render",value:function(){return r.a.createElement("div",{className:"menu__items"},r.a.createElement(E.b,{to:"/",className:"menu__items-item "},"Home"),r.a.createElement(E.b,{to:"/browse",className:"menu__items-item "},"Browse"),r.a.createElement(E.b,{to:"/guide",className:"menu__items-item "},"Guide"),this.props.loggedIn?r.a.createElement("div",{className:"item-right"},r.a.createElement(E.b,{to:"/dashboard",className:"menu__items-item m-right "},"Dashboard"),r.a.createElement(E.b,{to:"/logout",className:"menu__items-item m-right "},"Log Out")):r.a.createElement("div",{className:"item-right"},r.a.createElement(E.b,{to:"/login",className:"menu__items-item m-right "},"Log in"),r.a.createElement(E.b,{to:"/signup",className:"menu__items-item m-right"},"Sign up")))}}]),t}(n.Component),k=(a(64),function(){return r.a.createElement(r.a.Fragment,null,r.a.createElement("div",{className:"main__footer-container"},r.a.createElement("div",{className:"main__footer-row"},r.a.createElement("div",{className:"main__footer-column"},r.a.createElement("h4",{className:"main__footer-heading"},"About"),r.a.createElement("div",{className:"main__footer-links"},r.a.createElement(E.b,{to:"/",className:"footer-item"},"Jobs"),r.a.createElement(E.b,{to:"/",className:"footer-item"},"Contact Us"),r.a.createElement(E.b,{to:"/",className:"footer-item"},"Customer Support"),r.a.createElement(E.b,{to:"/",className:"footer-item"},"Future Plans"))),r.a.createElement("div",{className:"main__footer-column"},r.a.createElement("h4",{className:"main__footer-heading"},"Services"),r.a.createElement("div",{className:"main__footer-links"},r.a.createElement(E.b,{to:"/",className:"footer-item"},"Data Policy"),r.a.createElement(E.b,{to:"/",className:"footer-item"},"FAQ"),r.a.createElement(E.b,{to:"/",className:"footer-item"},"How To Access"),r.a.createElement(E.b,{to:"/",className:"footer-item"},"Advertise"))),r.a.createElement("div",{className:"main__footer-column"},r.a.createElement("h4",{className:"main__footer-heading"},"@Recipe Advisor"),r.a.createElement("p",null,"Project based on IEEE paper -Recommendation of Indian Cuisine Recipes based on Ingredients"),r.a.createElement("p",null,"Project Members - "),r.a.createElement("ul",null,r.a.createElement("li",null,"Mohammed Idrees - 1KN16IS015 "),r.a.createElement("li",null,"Rahul Deb Barma - 1KN16IS025"),r.a.createElement("li",null,"Rohit Kumar Mishra - 1KN16IS026"),r.a.createElement("li",null,"Utkarsh Mishra - 1KN16IS037")),r.a.createElement("p",null,"Under the guidance of - "),r.a.createElement("p",{style:{fontSize:"1rem",color:"yellow"}},"Mr. Kantharaju",r.a.createElement("br",null),"Prof. , Dept of ISE"),r.a.createElement("p",null,"All Rights Reserved. \xa92020")))))}),N=a(46),x=a.n(N),S=a(19),w=a(47),O=a(24),j=(a(65),function(){return r.a.createElement("div",{className:"main__container"},r.a.createElement("h1",{className:"main__title"},"Recipe Advisor ",r.a.createElement(O.b,{className:"icon"})),r.a.createElement("h3",{className:"sub-main__title"},"Make whatever you want whenever you want to."),r.a.createElement(E.b,{to:"/guide",className:"main__button"},"Get Started",r.a.createElement(w.a,{className:"icon"})))}),I=(a(66),a(13)),R=a.n(I),C=function(){var e=Object(o.a)(u.a.mark((function e(t){var a;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,R.a.post("/api/login",t);case 2:return a=e.sent,e.abrupt("return",a.data);case 4:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),P=function(e,t){try{return localStorage.setItem("user",e),localStorage.setItem("token",t),sessionStorage.setItem("user",e),sessionStorage.setItem("token",t),!0}catch(a){return!1}},D=function(){var e=Object(o.a)(u.a.mark((function e(t,a){var n,r,c;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.prev=0,n=Boolean(sessionStorage.getItem("user"))||!1,r=!!n&&sessionStorage.getItem("token"),e.next=5,R.a.post("/api/verify-token",{user:n,token:r});case 5:return c=e.sent,e.abrupt("return",c.data.value);case 9:return e.prev=9,e.t0=e.catch(0),e.abrupt("return",{error:e.t0});case 12:case"end":return e.stop()}}),e,null,[[0,9]])})));return function(t,a){return e.apply(this,arguments)}}();var L=function(e){Object(d.a)(a,e);var t=function(e){function t(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}return function(){var a,n=Object(f.a)(e);if(t()){var r=Object(f.a)(this).constructor;a=Reflect.construct(n,arguments,r)}else a=n.apply(this,arguments);return Object(p.a)(this,a)}}(a);function a(){var e;Object(l.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={users:{email:"",password:""},fail:void 0},e.handleSubmit=function(){var t=Object(o.a)(u.a.mark((function t(a){var n,r;return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return a.preventDefault(),n=!1,r=e.state.users,t.next=5,C(r);case 5:if("true"!==(n=t.sent).value){t.next=11;break}if(!P(n.username,n.token)){t.next=11;break}return t.next=10,e.setState({loggedIn:!0});case 10:return t.abrupt("return",e.props.updateUser());case 11:if(!1!==n.value){t.next=13;break}return t.abrupt("return",e.setState({fail:!0}));case 13:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e.updateValue=function(t){var a=t.target.name,n=e.state.users;n[a]=t.target.value,e.setState({fail:void 0,users:n})},e}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(o.a)(u.a.mark((function e(){return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.props.loggedIn;case 2:if(e.t1=e.sent,e.t0=!0===e.t1,e.t0){e.next=9;break}return e.next=7,this.state.loggedIn;case 7:e.t2=e.sent,e.t0=!0===e.t2;case 9:if(!e.t0){e.next=11;break}this.props.history.push("/dashboard");case 11:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this;return(r.a.createElement("div",{className:"login__container"},r.a.createElement("div",{className:"login__box"},r.a.createElement("div",{className:"login__title"},r.a.createElement("div",{className:"login__heading"},"Log In with email"),r.a.createElement("p",null,"If you are Existing Recipe Advisor user")),r.a.createElement("div",{className:"login__body"},r.a.createElement("form",{onSubmit:function(t){return e.handleSubmit(t)}},r.a.createElement("div",{className:"view__column"},r.a.createElement("input",{placeholder:"Email",type:"email",name:"email",onInput:function(t){return e.updateValue(t)},className:"input__box email",required:!0}),r.a.createElement("input",{placeholder:"Password",type:"password",name:"password",onInput:function(t){return e.updateValue(t)},className:"input__box password",required:!0,autoComplete:"true"}),this.state.fail?r.a.createElement("p",{className:"alert__box"},"Invalid Email or Password !! Try Again!"):null,r.a.createElement("input",{type:"submit",className:"input__box form__submit",value:"Sign In"})))))))}}]),a}(n.Component),A=(a(84),function(e){return R.a.post("/api/signup",e).then((function(e){return e.data}))});var V=function(e){Object(d.a)(a,e);var t=function(e){function t(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}return function(){var a,n=Object(f.a)(e);if(t()){var r=Object(f.a)(this).constructor;a=Reflect.construct(n,arguments,r)}else a=n.apply(this,arguments);return Object(p.a)(this,a)}}(a);function a(){var e;Object(l.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={users:{user_name:"",email:"",password:""},exist:!1},e.updateValue=function(t){var a=t.target.name,n=e.state.users;return n[a]=t.target.value,"email"===t.target.name&&e.state.exist&&e.setState({exist:!1}),e.setState({users:n})},e.handleSubmit=function(){var t=Object(o.a)(u.a.mark((function t(a){var n,r;return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return a.preventDefault(),n=!1,r=e.state.users,t.next=5,A(r);case 5:if("sucess"===(n=t.sent).value&&e.setState({exist:!1}),"exist"!==n.value){t.next=11;break}return t.abrupt("return",e.setState({exist:!0}));case 11:return t.next=13,P(n.username,n.token);case 13:if(!t.sent){t.next=17;break}return t.next=16,e.props.updateUser();case 16:return t.abrupt("return",e.props.history.push("/dashboard"));case 17:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(o.a)(u.a.mark((function e(){return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:!0===this.props.loggedIn&&this.props.history.push("/dashboard");case 1:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this;return(r.a.createElement("div",{className:"signup__container"},r.a.createElement("div",{className:"signup__box"},r.a.createElement("div",{className:"signup__title"},r.a.createElement("div",{className:"signup__heading"},"Sign up with email"),r.a.createElement(E.b,{to:"/login",className:"link__item"},"Existing Recipe Advisor user? Log In")),r.a.createElement("form",{onSubmit:function(t){return e.handleSubmit(t)}},r.a.createElement("div",{className:"view__column"},r.a.createElement("input",{placeholder:"Display Name",type:"text",name:"user_name",className:"input__box user_name",onInput:function(t){return e.updateValue(t)},required:!0}),r.a.createElement("input",{placeholder:"Email",type:"email",name:"email",className:"input__box email",onInput:function(t){return e.updateValue(t)},required:!0}),this.state.exist?r.a.createElement("p",{className:"alert__box "},"Email ID already exists!"):null,r.a.createElement("input",{placeholder:"Password",type:"password",name:"password",className:"input__box password",onInput:function(t){return e.updateValue(t)},pattern:"(?=.*[A-Z])(?=.*[@$!%*#?&])[A-Za-z\\d@$!%*#?&]{6,}",title:"6 character with an uppercase and a special character",autoComplete:"true",required:!0}),r.a.createElement("p",null,"Please provide a password with at least 6 characters. Your password must include at least 1 uppercase letter and a special character."),r.a.createElement("input",{type:"submit",className:"input__box form__submit",value:"Sign Up"}))))))}}]),a}(n.Component),z=function(e){var t=e.cuisine;return(r.a.createElement("div",{className:"recipe__card"},r.a.createElement("div",{className:"recipe__title"},r.a.createElement("h5",{className:"recipe__name"},t.name),r.a.createElement("p",{className:"recipe__rating"},parseFloat(t.ratings).toFixed(2)+" Stars")),r.a.createElement("div",{className:"recipe__content"},r.a.createElement("div",{className:"recipe__image"},r.a.createElement("img",{src:t.img_link,alt:t.name})," "),r.a.createElement("div",{className:"recipe__category"},r.a.createElement("h5",null,"Categories:"),t.breadcrumbs.map((function(e,t){return t<2?r.a.createElement("p",{key:t},e):null})))),r.a.createElement(E.b,{to:"/browse/recipe/".concat(t.id),className:"recipe__button "},"Get Recipe !")))},M=function(e){var t=e.cuisines;return r.a.createElement("div",{className:"recipe__row"},t.map((function(e){return r.a.createElement(z,{key:e.id,cuisine:e})})))};var F=function(e){var t=e.items,a=e.onPageChange,n=e.pageSize,c=e.currentPage,s=function(){var e=arguments.length>0&&void 0!==arguments[0]?arguments[0]:1,t=arguments.length>1?arguments[1]:void 0,a=arguments.length>2?arguments[2]:void 0,n=arguments.length>3?arguments[3]:void 0,r=[],c=Math.ceil(a/t)||1,s=1;c>10&&(s=e>Math.ceil(c/2)?1:e,e=n-5<e?1:e);for(var i=s;i<c;i++)r.push(parseInt(i));if(n>Math.ceil(c/2)&&c>10){var u=r.indexOf(n-5),o=r.splice(u,6);return o.unshift("..."),o.unshift(1),o[o.length-1]!==c-1&&(o.push(".."),o.push(c-1)),o}if(c>10){var l=r.splice(5);r.push("..."),1!==r[0]&&(r.unshift(".."),r.unshift(1)),r.push(l.pop())}return r}(e.startValue,t,n,c);return r.a.createElement("div",{className:"menu__pages"},s.map((function(e){var t=e===c?{backgroundColor:"White",color:"#ff0000"}:{color:"#ff0000"};return"..."===e||".."===e?r.a.createElement("div",{key:e,className:"page_no"},e):r.a.createElement(E.b,{key:e,to:"/browse/".concat(e),onClick:function(){return a(e)},style:t,className:e===c?"active page_no":"page_no"},e)})))},q=function(){var e=Object(o.a)(u.a.mark((function e(t){var a;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,R.a.get("".concat("/api/get-recipe","/").concat(t));case 2:return a=e.sent,e.abrupt("return",a.data);case 4:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),U=function(){var e=Object(o.a)(u.a.mark((function e(t){var a;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,R.a.get("".concat("/api/recipe/","/").concat(t));case 2:return a=e.sent,e.abrupt("return",a.data);case 4:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}(),T=a(48),B=function(){return r.a.createElement("div",{className:"loading__container"},r.a.createElement(T.a,{className:"loader"}))},Q=function(){var e=Object(o.a)(u.a.mark((function e(t,a){var n;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,R.a.post("/api/search",{query:t,page_no:a});case 2:return n=e.sent,e.abrupt("return",n.data);case 4:case"end":return e.stop()}}),e)})));return function(t,a){return e.apply(this,arguments)}}(),G=a(22),K=function(e){var t=e.backArea,a=e.handleClick,n=Object(S.g)();return r.a.createElement("div",{className:"failed__container"},r.a.createElement("button",{onClick:function(){return function(e,t){var a=arguments.length>2&&void 0!==arguments[2]?arguments[2]:void 0;return void 0!==a&&a(),e.push(t)}(n,t,a)},className:"goback-button"},r.a.createElement(G.a,null)),r.a.createElement("div",{className:"failed__body"},r.a.createElement("h2",{className:"failed__message"},"Not Found !"),r.a.createElement(G.c,{className:"failed-icon"})))};var H=function(e){Object(d.a)(a,e);var t=function(e){function t(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}return function(){var a,n=Object(f.a)(e);if(t()){var r=Object(f.a)(this).constructor;a=Reflect.construct(n,arguments,r)}else a=n.apply(this,arguments);return Object(p.a)(this,a)}}(a);function a(){var e;Object(l.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={currentPage:1,cuisines:[],isLoading:!0,pageSize:1,startValue:1,searchQuery:"",failed:!1},e.loading=function(){return[e.setState({isLoading:!0})]},e.handlePageChange=function(){var t=Object(o.a)(u.a.mark((function t(a){var n,r,c,s,i,o,l;return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:if(n=e.state,r=n.currentPage,c=n.cuisines,s=n.pageSize,i=n.startValue,o=n.searchQuery,!(a>0)){t.next=21;break}if(r=a,i=a,e.loading(),!(o.length>0)){t.next=11;break}return t.next=8,Q(o,r);case 8:c=t.sent,t.next=14;break;case 11:return t.next=13,q(r);case 13:c=t.sent;case 14:if(!(c.length>0&&null!=c[c.length-1].totalSize)){t.next=20;break}return l=c.pop(),s=parseInt(l.totalSize),t.abrupt("return",e.setState({currentPage:r,pageSize:s,cuisines:c,isLoading:!1,startValue:i,failed:!1}));case 20:return t.abrupt("return",e.setState({isLoading:!1,failed:!0}));case 21:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e.handleSearch=function(){var t=Object(o.a)(u.a.mark((function t(a){var n;return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return e.state.searchQuery,n=a.target.value,t.next=4,e.setState({searchQuery:n});case 4:return t.next=6,e.searchRecipe();case 6:return t.abrupt("return",t.sent);case 7:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e.handleFailClick=Object(o.a)(u.a.mark((function t(){return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,e.setState({searchQuery:""});case 2:return t.next=4,e.searchRecipe();case 4:return t.abrupt("return",t.sent);case 5:case"end":return t.stop()}}),t)}))),e.searchRecipe=Object(o.a)(u.a.mark((function t(){var a,n,r,c,s,i;return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return a=e.state,n=a.searchQuery,r=a.cuisines,c=a.pageSize,s=a.startValue,s=1,t.next=4,e.setState({isSearching:!0});case 4:return t.next=6,Q(n,s);case 6:return r=t.sent,i=r.pop(),c=i.totalSize,t.next=11,e.setState({cuisines:r,isLoading:!1,pageSize:c,startValue:s,currentPage:1,failed:!1,isSearching:!1});case 11:if(0!==c){t.next=13;break}return t.abrupt("return",e.setState({isLoading:!1,startValue:s,currentPage:1,failed:!0,isSearching:!1}));case 13:case"end":return t.stop()}}),t)}))),e}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(o.a)(u.a.mark((function e(){var t,a,n,r,c,s;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=this.state,a=t.cuisines,n=t.pageSize,r=t.currentPage,c=t.startValue,r=this.props.match.params.id&&this.props.match.params.id>0?parseInt(this.props.match.params.id):r,c=r,e.next=5,q(r);case 5:if(a=e.sent,s=a.pop(),!((n=s.totalSize)>0&&0!==a.length)){e.next=10;break}return e.abrupt("return",this.setState({cuisines:a,isLoading:!1,pageSize:n,startValue:c,currentPage:r,failed:!1,isSearching:!1}));case 10:return e.abrupt("return",this.setState({isLoading:!1,failed:!0}));case 11:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this,t=this.state,a=t.cuisines,n=t.isLoading,c=t.pageSize,s=t.currentPage,i=t.startValue,u=t.searchQuery,o=t.failed,l=t.isSearching;return n?r.a.createElement(B,null):r.a.createElement(r.a.Fragment,null,r.a.createElement("div",{className:"search__list"},r.a.createElement("form",{onSubmit:function(e){e.preventDefault()}},r.a.createElement("input",{type:"text",onChange:function(t){return e.handleSearch(t)},className:"input__box",name:"search",value:u,placeholder:"Search Cuisine!"}))),l?r.a.createElement(B,null):r.a.createElement(r.a.Fragment,null,o?r.a.createElement(K,{backArea:"/browse",handleClick:this.handleFailClick}):r.a.createElement("div",{className:"recipe__container"},r.a.createElement("div",{className:"recipe__list"},r.a.createElement(M,{cuisines:a})),r.a.createElement("div",{className:"pagination"},r.a.createElement(F,{items:a.length,onPageChange:this.handlePageChange,pageSize:c,currentPage:s,startValue:i})))))}}]),a}(n.Component),J=(a(85),a(28));var Z=function(e){Object(d.a)(a,e);var t=function(e){function t(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}return function(){var a,n=Object(f.a)(e);if(t()){var r=Object(f.a)(this).constructor;a=Reflect.construct(n,arguments,r)}else a=n.apply(this,arguments);return Object(p.a)(this,a)}}(a);function a(){var e;Object(l.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={ingredients:[""]},e.updateValue=function(){var t=Object(o.a)(u.a.mark((function t(a){var n,r;return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return n=parseInt(a.target.name),(r=e.state.ingredients)[n]=a.target.value,t.abrupt("return",e.setState({ingredients:r}));case 4:case"end":return t.stop()}}),t)})));return function(e){return t.apply(this,arguments)}}(),e.addInput=function(){var t=e.state.ingredients;t.length<1?t=[""]:t.length<=10&&t.push(""),e.setState({ingredients:t})},e.removeInput=function(t){var a=e.state.ingredients,n=parseInt(t.target.name);return isNaN(n)&&(n=parseInt(t.currentTarget.name)),a=a.filter((function(e,t){return t!==n?e:null})),e.setState({ingredients:a})},e.handleSubmit=function(t){t.preventDefault();var a=e.state.ingredients;if(a.length>0)return e.props.history.push("/guide/results/q=".concat(a))},e}return Object(m.a)(a,[{key:"render",value:function(){var e=this,t=this.state.ingredients;return r.a.createElement(r.a.Fragment,null,r.a.createElement("div",{className:"guide__container"},r.a.createElement("div",{className:"recipe__guess-form"},r.a.createElement("form",{action:"",onSubmit:function(t){return e.handleSubmit(t)},className:"input__form"},r.a.createElement("div",{className:"guess-form__header"},r.a.createElement("h3",{className:"sub-main__title"},"Add the Ingredients to get recommendations !")),r.a.createElement("div",{className:"ingredient__container"},t.map((function(t,a){return a>10?r.a.createElement("h2",{key:a,className:"input__box"},"Ingredients Limit Exceeded !"):r.a.createElement("div",{key:a,className:"input__container"},r.a.createElement("input",{key:a,type:"text",className:"input__box",name:a,placeholder:"Add Ingredient ".concat(a+1),onChange:function(t){return e.updateValue(t)},value:t,required:!0}),r.a.createElement("button",{type:"button",name:a,className:"add__link-button",onClick:function(t){return e.removeInput(t)}},r.a.createElement(J.a,null)))}))),r.a.createElement("button",{type:"button",className:"add__link-button",onClick:this.addInput},r.a.createElement(J.b,null)),r.a.createElement("div",{className:"submit__container"},r.a.createElement("input",{type:"submit",value:"Get Recipe !",className:"input__box form__submit"}))))))}}]),a}(n.Component),$=function(){var e=Object(o.a)(u.a.mark((function e(t){var a;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,R.a.post("/api/predict",{queryString:t});case 2:return a=e.sent,e.abrupt("return",a.data);case 4:case"end":return e.stop()}}),e)})));return function(t){return e.apply(this,arguments)}}();var W=function(e){Object(d.a)(a,e);var t=function(e){function t(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}return function(){var a,n=Object(f.a)(e);if(t()){var r=Object(f.a)(this).constructor;a=Reflect.construct(n,arguments,r)}else a=n.apply(this,arguments);return Object(p.a)(this,a)}}(a);function a(){var e;Object(l.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={recipe:[],isLoading:!0,ingredients:[]},e}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(o.a)(u.a.mark((function e(){var t,a,n,r,c,s;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(t=this.props,a=t.location,n=t.match,r=t.history,c=a.state,s=n.params.query?n.params.query.split(","):0,c||!(s.length>0)){e.next=9;break}return e.next=6,$(s);case 6:c=e.sent,e.next=11;break;case 9:return e.next=11,r.push("/guide");case 11:return e.abrupt("return",this.setState({recipe:c,ingredients:s,isLoading:!1}));case 12:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this,t=this.state,a=t.recipe;return t.isLoading&&0===a.length?r.a.createElement(B,null):r.a.createElement("div",{className:"recipe__container"},r.a.createElement("button",{onClick:function(){return e.props.history.push("/guide")},className:"goback-button"},r.a.createElement(O.a,null)),r.a.createElement("div",{className:"recipe__guide"},a.map((function(t){return r.a.createElement("div",{key:t.id,className:"recipe__container"},r.a.createElement("div",{className:"recipe__head"},r.a.createElement("h1",null,t.name)),r.a.createElement("div",{className:"recipe__body"},r.a.createElement("div",{className:"recipe__image"},r.a.createElement("img",{src:t.img_link,alt:t.name})),r.a.createElement("div",{className:"recipe__ingredients"},r.a.createElement("h2",null,"Ingredients in Recipe:"),r.a.createElement("ul",null,t.ingredients&&t.ingredients.map((function(t,a){return r.a.createElement("li",{key:t.name+a,className:e.state.ingredients.map((function(e){return String(t.phrase).includes(String(e).toLowerCase())})).some((function(e){return e}))?"ingredients item-checked":"ingredients not-checked"},t.phrase)}))))),r.a.createElement("div",{className:"recipe__info"},r.a.createElement(E.b,{className:"recipe__button",to:"/browse/recipe/".concat(t.id)},"Get Info!")))}))))}}]),a}(n.Component),Y=(a(86),a(18));a(40);var X=function(e){Object(d.a)(a,e);var t=function(e){function t(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}return function(){var a,n=Object(f.a)(e);if(t()){var r=Object(f.a)(this).constructor;a=Reflect.construct(n,arguments,r)}else a=n.apply(this,arguments);return Object(p.a)(this,a)}}(a);function a(){var e;Object(l.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={username:void 0,success:!1,firstLogin:!1,liked:[]},e}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(o.a)(u.a.mark((function e(){var t,a,n,r,c;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,this.props.loggedIn;case 2:if(e.t0=e.sent,!1!==e.t0){e.next=7;break}return e.abrupt("return",this.props.history.push("/login"));case 7:if(t=this.state,a=t.username,n=t.firstLogin,a=localStorage.getItem("user")||a,(r="false"!==localStorage.getItem("firstLogin"))&&void 0===a?localStorage.setItem("firstLogin",!0):localStorage.setItem("firstLogin",!1),(r||n)&&void 0!==a&&Y.b.success("Hello ".concat(a,"! let's Get you Started !"),{position:Y.b.POSITION.TOP_RIGHT,autoClose:2500,hideProgressBar:!0,closeButton:!1,className:"greet__user"}),c=this.state.liked,void 0===a){e.next=17;break}return e.next=16,this.props.liked();case 16:c=e.sent;case 17:return e.abrupt("return",this.setState({username:a,firstLogin:!1,liked:c}));case 18:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this.state,t=e.username,a=e.liked;return Boolean(t)?r.a.createElement("div",{className:"dashboard__container"},r.a.createElement("div",{className:"dashboard__heading"},r.a.createElement("h2",null,"Recipe Recommendation based on your choices!")),r.a.createElement("div",{className:"dashboard__body"}),a&&a.length>0?r.a.createElement(r.a.Fragment,null,r.a.createElement("div",{className:"dashboard__heading liked"},r.a.createElement("h2",null,"Recipe liked based on your past history!")),r.a.createElement("div",{className:"dashboard__body--wrapper"},r.a.createElement("div",{className:"dashboard__body liked"},a.map((function(e){return r.a.createElement("div",{key:e.id,className:"recipe__liked-list"},r.a.createElement(E.b,{to:"/browse/recipe/".concat(e.id),className:"recipe__button"},e.name),r.a.createElement("img",{className:"recipe_image",src:e.img_link,alt:e.name}))}))))):null):r.a.createElement(B,null)}}]),a}(n.Component),ee=a(29),te=a.n(ee),ae=a(49),ne=function(){var e=Object(ae.a)(te.a.mark((function e(){var t;return te.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,D();case 2:return t=e.sent,e.abrupt("return",t);case 4:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}(),re=function(e){return localStorage.clear(),sessionStorage.clear(),e.updateUser(),r.a.createElement(S.a,{to:"/login"})},ce=(a(88),function(){var e=Object(o.a)(u.a.mark((function e(){var t,a,n,r,c,s=arguments;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:if(t=s.length>0&&void 0!==s[0]?s[0]:null,a=s.length>1&&void 0!==s[1]?s[1]:null,n=sessionStorage.getItem("user")||!1,r=!!n&&sessionStorage.getItem("token")){e.next=6;break}return e.abrupt("return",!1);case 6:return e.next=8,R.a.post("/api/userLikings",{user:n,token:r,liked:t,recipe_id:a});case 8:return c=e.sent,e.abrupt("return",c.data);case 10:case"end":return e.stop()}}),e)})));return function(){return e.apply(this,arguments)}}());var se=function(e){Object(d.a)(a,e);var t=function(e){function t(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}return function(){var a,n=Object(f.a)(e);if(t()){var r=Object(f.a)(this).constructor;a=Reflect.construct(n,arguments,r)}else a=n.apply(this,arguments);return Object(p.a)(this,a)}}(a);function a(){var e;Object(l.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={cuisine:[],loading:!0,liked:!1,failed:!1},e.onClick=Object(o.a)(u.a.mark((function t(){var a,n,r;return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return a=e.state,n=a.liked,r=a.cuisine,t.next=3,ne();case 3:if(!t.sent){t.next=12;break}return n=!n,t.next=7,ce(n,r.id);case 7:if(!0!==t.sent.value){t.next=10;break}return t.abrupt("return",e.setState({liked:n}));case 10:t.next=13;break;case 12:Y.b.error("Log in required",{position:Y.b.POSITION.TOP_CENTER,autoClose:1e3,hideProgressBar:!0,closeButton:!1,className:"login__error"});case 13:case"end":return t.stop()}}),t)}))),e}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(o.a)(u.a.mark((function e(){var t,a,n,r,c;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=this.state,a=t.cuisine,n=t.liked,r=parseInt(this.props.match.params.id),e.next=4,U(r);case 4:return a=e.sent,e.next=7,ce();case 7:if((c=e.sent)&&c.liked_recipe.find((function(e){return e===parseInt(r)}))&&(n=!0),!a||a.id!==r){e.next=11;break}return e.abrupt("return",this.setState({cuisine:a,loading:!1,liked:n}));case 11:return e.abrupt("return",this.setState({loading:!1,failed:!0}));case 12:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this.state,t=e.cuisine,a=e.loading,n=e.liked,c=e.failed;if(a)return r.a.createElement(B,null);if(c)return r.a.createElement(K,{backArea:"/browse"});var s=n?{color:"#fdcf58 "}:{color:"inherit"};return(r.a.createElement("div",{className:"recipe__container"},r.a.createElement("div",{className:"recipe__head"},r.a.createElement("h1",null,t.name),r.a.createElement(G.b,{style:s,onClick:this.onClick})),r.a.createElement("div",{className:"recipe__body"},r.a.createElement("div",{className:"recipe__image"},r.a.createElement("img",{src:t.img_link,alt:t.name})),r.a.createElement("div",{className:"recipe__ingredients"},r.a.createElement("h2",{className:"recipe__heading"},"Ingredients in Recipe:"),r.a.createElement("ul",null,t.ingredients&&t.ingredients.map((function(e,t){return r.a.createElement("li",{key:t,className:"ingredients"},e.phrase)}))))),r.a.createElement("h2",{className:"recipe__heading"},"Nutrition Values"),r.a.createElement("div",{className:"recipe__info"},r.a.createElement("p",null,"Serving Count :"+t.serving_count),t.nutrition.map((function(e){return 0!==e[Object.keys(e)].value?r.a.createElement("p",{key:Object.keys(e)[0]},Object.keys(e)+" : "+e[Object.keys(e)].value+" "+e[Object.keys(e)].unit):null}))),r.a.createElement("div",{className:"recipe__instructions"},r.a.createElement("h2",{className:"recipe__heading"},"Instructions"),r.a.createElement("ol",null,t.description&&t.description.map((function(e){return r.a.createElement("li",{key:e.phrase},e.phrase)}))))))}}]),a}(n.Component);Y.b.configure();var ie=function(e){Object(d.a)(a,e);var t=function(e){function t(){if("undefined"===typeof Reflect||!Reflect.construct)return!1;if(Reflect.construct.sham)return!1;if("function"===typeof Proxy)return!0;try{return Date.prototype.toString.call(Reflect.construct(Date,[],(function(){}))),!0}catch(e){return!1}}return function(){var a,n=Object(f.a)(e);if(t()){var r=Object(f.a)(this).constructor;a=Reflect.construct(n,arguments,r)}else a=n.apply(this,arguments);return Object(p.a)(this,a)}}(a);function a(){var e;Object(l.a)(this,a);for(var n=arguments.length,r=new Array(n),c=0;c<n;c++)r[c]=arguments[c];return(e=t.call.apply(t,[this].concat(r))).state={loggedIn:!1,isLoading:!0,error:[]},e.updateUser=Object(o.a)(u.a.mark((function t(){var a;return u.a.wrap((function(t){for(;;)switch(t.prev=t.next){case 0:return t.next=2,ne();case 2:if(t.t0=t.sent,t.t0){t.next=5;break}t.t0=!1;case 5:return a=t.t0,t.abrupt("return",e.setState({loggedIn:a}));case 7:case"end":return t.stop()}}),t)}))),e.updateLikes=Object(o.a)(u.a.mark((function e(){var t,a,n,r,c,s,i,o;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return t=[],e.next=3,ce();case 3:a=(a=e.sent).liked_recipe,n=!0,r=!1,c=void 0,e.prev=8,s=a[Symbol.iterator]();case 10:if(n=(i=s.next()).done){e.next=20;break}return o=i.value,e.t0=t,e.next=15,U(o);case 15:e.t1=e.sent,e.t0.push.call(e.t0,e.t1);case 17:n=!0,e.next=10;break;case 20:e.next=26;break;case 22:e.prev=22,e.t2=e.catch(8),r=!0,c=e.t2;case 26:e.prev=26,e.prev=27,n||null==s.return||s.return();case 29:if(e.prev=29,!r){e.next=32;break}throw c;case 32:return e.finish(29);case 33:return e.finish(26);case 34:return e.abrupt("return",t);case 35:case"end":return e.stop()}}),e,null,[[8,22,26,34],[27,,29,33]])}))),e}return Object(m.a)(a,[{key:"componentDidMount",value:function(){var e=Object(o.a)(u.a.mark((function e(){var t,a;return u.a.wrap((function(e){for(;;)switch(e.prev=e.next){case 0:return e.next=2,ne();case 2:if(t=e.sent,this.state.error,!t.error){e.next=8;break}return a=String(t.error).split(10),Y.b.error(a[0],{position:Y.b.POSITION.TOP_CENTER}),e.abrupt("return",this.setState({error:a,isLoading:!1}));case 8:return e.abrupt("return",this.setState({loggedIn:t,isLoading:!1}));case 9:case"end":return e.stop()}}),e,this)})));return function(){return e.apply(this,arguments)}}()},{key:"render",value:function(){var e=this,t=this.state,a=t.loggedIn,n=t.isLoading,c=t.error,s=r.a.createElement("div",{className:"bg__video"},r.a.createElement("video",{loop:!0,muted:!0,autoPlay:!0,className:"fullscreen-bg__video",title:"./Images/recipe-background.jpeg"},r.a.createElement("source",{src:x.a,type:"video/mp4"})));return n?r.a.createElement(r.a.Fragment,null,s,r.a.createElement("div",{className:"App"},c[0]?r.a.createElement(Y.a,null):null,r.a.createElement(B,null))):r.a.createElement(r.a.Fragment,null,s,r.a.createElement("div",{className:"App"},r.a.createElement(y,{loggedIn:a}),r.a.createElement(r.a.Fragment,null,r.a.createElement(S.d,null,r.a.createElement(S.b,{exact:!0,path:"/dashboard",component:function(t){return r.a.createElement(X,Object.assign({},t,{loggedIn:a,liked:e.updateLikes}))},className:" item"}),r.a.createElement(S.b,{path:"/browse/:id?",component:H,className:" item",exact:!0}),r.a.createElement(S.b,{path:"/logout",component:function(t){return r.a.createElement(re,Object.assign({updateUser:e.updateUser},t))},className:" item",exact:!0}),r.a.createElement(S.b,{path:"/guide/results/q=:query?",component:W,className:" item",exact:!0}),r.a.createElement(S.b,{path:"/guide",component:Z,className:" item"}),r.a.createElement(S.b,{path:"/login",component:function(t){return r.a.createElement(L,Object.assign({updateUser:e.updateUser,loggedIn:a},t))},className:" item",exact:!0}),r.a.createElement(S.b,{path:"/signup",component:function(t){return r.a.createElement(V,Object.assign({loggedIn:a,updateUser:e.updateUser},t))},className:" item",exact:!0}),r.a.createElement(S.b,{path:"/browse/recipe/:id/:tab?",className:" item",component:se}),r.a.createElement(S.b,{path:"/",component:j,className:" item"}),r.a.createElement(S.b,{component:j}))),r.a.createElement(k,null)))}}]),a}(n.Component),ue=Object(S.h)((function(e){var t=e.children,a=e.location.pathname;return Object(n.useEffect)((function(){window.scrollTo({top:0,left:0,behavior:"smooth"})}),[a]),t||null}));s.a.render(r.a.createElement(E.a,null,r.a.createElement(ue,null,r.a.createElement(ie,null))),document.getElementById("root"))}},[[52,1,2]]]);
//# sourceMappingURL=main.d4b1223e.chunk.js.map