(function(t){function e(e){for(var s,r,o=e[0],l=e[1],c=e[2],m=0,d=[];m<o.length;m++)r=o[m],n[r]&&d.push(n[r][0]),n[r]=0;for(s in l)Object.prototype.hasOwnProperty.call(l,s)&&(t[s]=l[s]);u&&u(e);while(d.length)d.shift()();return i.push.apply(i,c||[]),a()}function a(){for(var t,e=0;e<i.length;e++){for(var a=i[e],s=!0,o=1;o<a.length;o++){var l=a[o];0!==n[l]&&(s=!1)}s&&(i.splice(e--,1),t=r(r.s=a[0]))}return t}var s={},n={app:0},i=[];function r(e){if(s[e])return s[e].exports;var a=s[e]={i:e,l:!1,exports:{}};return t[e].call(a.exports,a,a.exports,r),a.l=!0,a.exports}r.m=t,r.c=s,r.d=function(t,e,a){r.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:a})},r.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},r.t=function(t,e){if(1&e&&(t=r(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var a=Object.create(null);if(r.r(a),Object.defineProperty(a,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var s in t)r.d(a,s,function(e){return t[e]}.bind(null,s));return a},r.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return r.d(e,"a",e),e},r.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},r.p="/";var o=window["webpackJsonp"]=window["webpackJsonp"]||[],l=o.push.bind(o);o.push=e,o=o.slice();for(var c=0;c<o.length;c++)e(o[c]);var u=l;i.push([0,"chunk-vendors"]),a()})({0:function(t,e,a){t.exports=a("56d7")},"56d7":function(t,e,a){"use strict";a.r(e);a("cadf"),a("551c"),a("f751"),a("097d");var s=a("2b0e"),n=a("8a03"),i=a.n(n),r=(a("5abe"),a("a23f"),function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"clearfix"},[a("router-view")],1)}),o=[],l=(a("5c0b"),a("2877")),c={},u=Object(l["a"])(c,r,o,!1,null,null,null),m=u.exports,d=a("8c4f"),h=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},v=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"hero is-primary is-large"},[a("div",{staticClass:"hero-body"},[a("div",{staticClass:"container"},[a("h1",{staticClass:"title"},[t._v("\n        Welcome to HArnESS!\n      ")]),a("h2",{staticClass:"subtitle"},[t._v("\n        An open source manual evaluation software for abstractive summarization!\n      ")])])])])}],p={name:"Home"},f=p,g=(a("9f7d"),Object(l["a"])(f,h,v,!1,null,"c93b39a8",null)),_=g.exports,b=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("nav",{staticClass:"navbar",attrs:{role:"navigation","aria-label":"main navigation"}},[a("div",{staticClass:"container is-fluid"},[t._m(0),a("div",{staticClass:"navbar-menu",attrs:{id:"navbarBasicExample"}},[a("div",{staticClass:"navbar-start"},[a("div",{staticClass:"navbar-item has-dropdown is-hoverable"},[a("a",{staticClass:"navbar-link"},[t._v("\n                Projects\n              ")]),a("div",{staticClass:"navbar-dropdown"},[a("router-link",{staticClass:"navbar-item",attrs:{to:{name:"new"}}},[t._v("\n                  New...\n                ")]),a("router-link",{staticClass:"navbar-item",attrs:{to:{name:"manage"}}},[t._v("\n                  Manage...\n                ")])],1)])])])])]),a("router-view")],1)},y=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"navbar-brand"},[a("a",{staticClass:"navbar-item",attrs:{href:"/"}},[t._v("\n          Summ-Eval\n        ")])])}],k={name:"admin"},C=k,w=Object(l["a"])(C,b,y,!1,null,null,null),x=w.exports,j=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container"},[a("div",{staticClass:"tile is-ancestor"},[a("div",{staticClass:"tile is-parent"},[a("div",{staticClass:"tile is-child tabs"},[a("ul",[a("li",{class:{"is-active":t.isActive.annotation},on:{click:function(e){return t.toggleActive("annotation")}}},[a("router-link",{attrs:{to:{name:"newAnnotation"}}},[t._v("Annotation")])],1),a("li",{class:{"is-active":t.isActive.evaluation},on:{click:function(e){return t.toggleActive("evaluation")}}},[a("router-link",{attrs:{to:{name:"newEvaluation"}}},[t._v("Evaluation")])],1)])])])]),a("div",{staticClass:"tile is-ancestor"},[a("div",{staticClass:"tile is-parent is-5"},[a("div",{staticClass:"tile is-child"},[a("router-view")],1)])])])},T=[],P={name:"NewProject",data:function(){return{isActive:{annotation:!0,evaluation:!1}}},methods:{toggleActive:function(t){"annotation"===t?(this.isActive.annotation=!0,this.isActive.evaluation=!1):"evaluation"===t&&(this.isActive.evaluation=!0,this.isActive.annotation=!1)}}},$=P,E=Object(l["a"])($,j,T,!1,null,"56b7ad3e",null),S=E.exports,A=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",[a("label",{staticClass:"label"},[t._v("Create a New Project for Manual Evaluation")]),a("b-field",{attrs:{horizontal:"",label:"Name",message:"Please enter the project name"}},[a("b-input",{attrs:{name:"name",expanded:""},model:{value:t.project.name,callback:function(e){t.$set(t.project,"name",e)},expression:"project.name"}})],1),a("b-field",{attrs:{horizontal:"",label:"Category"}},[a("b-select",{attrs:{placeholder:"Select evaluation category",icon:"wrench","icon-pack":"fas"},model:{value:t.project.category,callback:function(e){t.$set(t.project,"category",e)},expression:"project.category"}},[a("option",{attrs:{value:"Fluency"}},[t._v("Fluency")])])],1),t.datasets?a("b-field",{attrs:{horizontal:"",label:"Dataset"}},[a("b-select",{attrs:{placeholder:"Select a dataset",icon:"database","icon-pack":"fas"},model:{value:t.project.dataset,callback:function(e){t.$set(t.project,"dataset",e)},expression:"project.dataset"}},t._l(t.datasets,function(e){return a("option",{key:e.name,domProps:{value:e}},[t._v("\n              "+t._s(e.name)+"\n            ")])}),0)],1):t._e(),t.project.dataset?a("b-field",{attrs:{horizontal:"",label:"Summary Group"}},[a("b-select",{attrs:{placeholder:"Select a summary group",icon:"file","icon-pack":"fas"},model:{value:t.project.summ_group,callback:function(e){t.$set(t.project,"summ_group",e)},expression:"project.summ_group"}},t._l(t.project.dataset.summ_groups,function(e){return a("option",{key:e.name,domProps:{value:e}},[t._v(t._s(e.name))])}),0)],1):t._e(),a("b-field",{attrs:{horizontal:"",label:"# of evaluation",message:"Number of evaluation per document"}},[a("b-input",{attrs:{name:"total_exp_results",type:"number"},model:{value:t.project.total_exp_results,callback:function(e){t.$set(t.project,"total_exp_results",t._n(e))},expression:"project.total_exp_results"}})],1),a("button",{staticClass:"button is-primary",on:{click:t.createProject}},[t._v("Create Project")])],1)},M=[],O=a("bc3a"),z={name:"NewEvaluation",data:function(){return{datasets:null,project:{name:"",dataset:null,summ_group:null,category:null,total_exp_results:1}}},methods:{createProject:function(){var t=this;O.put("admin/project/evaluation",this.project).then(function(){t.$toast.open({message:"Project created!",type:"is-success"}),t.$router.push({name:"manage"})}).catch(function(){t.$toast.open({message:"Project is not created! Something is wrong",type:"is-danger"})})}},mounted:function(){var t=this;O.get("admin/dataset").then(function(e){404===e.status?t.$toast.open({message:e.statusText,type:"is-danger"}):t.datasets=e.data}).catch(function(e){t.$toast.open({message:"".concat(e),type:"is-danger"})})}},F=z,R=Object(l["a"])(F,A,M,!1,null,"54210df0",null),D=R.exports,q=function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"container home"},[a("div",{staticClass:"columns",style:{display:t.display.landing}},[a("div",{staticClass:"column is-8 is-offset-2 box content"},[a(t.dynamicLanding,{tag:"component"}),a("div",{attrs:{align:"center"}},[a("button",{staticClass:"button is-primary is-large",staticStyle:{"margin-bottom":"2rem"},on:{click:function(e){return t.closeLanding()}}},[t._v("I consent")])])],1)]),a("div",{staticClass:"columns",style:{display:t.display.content}},[a("div",{staticClass:"column is-8 is-offset-2 box content"},[a("div",{staticClass:"box summary"},[a("div",{staticClass:"content"},[a("h1",{attrs:{align:"center"}},[t._v("Please don't refresh the page.")]),a("hr"),a("h5",{staticClass:"my-header"},[t._v("Assess the following summary.")]),t.summaries?a("div",[a("p",{staticClass:"my-summary"},[t._v("\n                            "+t._s(t.summaryText)+"\n                          ")])]):t._e(),a("hr"),t._m(0),a("p",[t._v("\n                          Hover the mouse on top of the\n                          "),a("b-tooltip",{attrs:{label:"Don't forget to enter the m_turk code\n                                  at the end of the session."}},[a("b-icon",{attrs:{pack:"fas",icon:"info-circle",size:"is-small"}})],1),t._v(" to see more information.\n                      ")],1),a("p",{staticClass:"my-text"},[a("b-tooltip",{attrs:{label:"How much trouble did you have identifying\n                                  the referents of nounphrases in this summary?\n                                  Are there nouns, pronouns or personal names that are\n                                  not well-specified?"}},[a("b-icon",{attrs:{pack:"fas",icon:"info-circle",size:"is-small"}})],1),t._v("\n                        The summary has a "),a("strong",[t._v("clear reference")]),t._v(".\n                      ")],1),a("div",{staticClass:"level",staticStyle:{"margin-bottom":"1.8rem","margin-top":"1.8rem"},attrs:{align:"center"}},[t._m(1),a("span",{staticClass:"level-item"},[t.show?a("vue-slider",{attrs:{min:"1",max:"100",width:"100%"},model:{value:t.recall,callback:function(e){t.recall=e},expression:"recall"}}):t._e()],1),t._m(2)]),a("p",{staticClass:"my-text"},[a("b-tooltip",{attrs:{label:"Are there any obviously ungrammatical sentences,\n                                  e.g.,missing components, unrelated fragments or any other\n                                  grammar-related problem that makes the\n                                  text difficult to read? "}},[a("b-icon",{attrs:{pack:"fas",icon:"info-circle",size:"is-small"}})],1),t._v("\n                          The summary is "),a("strong",[t._v("grammatically")]),t._v(" correct.")],1),a("div",{staticClass:"level",staticStyle:{"margin-bottom":"1.8rem","margin-top":"1.8rem"},attrs:{align:"center"}},[t._m(3),a("span",{staticClass:"level-item"},[t.show?a("vue-slider",{attrs:{min:"1",max:"100",width:"100%"},model:{value:t.precision,callback:function(e){t.precision=e},expression:"precision"}}):t._e()],1),t._m(4)]),a("p",{staticClass:"my-text"},[a("b-tooltip",{attrs:{label:"Are there any datelines, system-internal\n                            formatting or capitalization errors that can make the reading\n                            of the summary difficult?"}},[a("b-icon",{attrs:{pack:"fas",icon:"info-circle",size:"is-small"}})],1),t._v("\n                        The summary has no noticeable "),a("strong",[t._v("formatting problem")]),t._v(".")],1),a("div",{staticClass:"level",staticStyle:{"margin-bottom":"1.8rem","margin-top":"1.8rem"},attrs:{align:"center"}},[t._m(5),a("span",{staticClass:"level-item"},[t.show?a("vue-slider",{attrs:{min:"1",max:"100",width:"100%"},model:{value:t.precision,callback:function(e){t.precision=e},expression:"precision"}}):t._e()],1),t._m(6)]),a("button",{staticClass:"button is-primary",on:{click:t.prev}},[t._v("\n                        Prev\n                      ")]),a("strong",[t._v("\n                        "+t._s(t.page.current)+"/"+t._s(t.page.total)+"\n                        ")]),a("button",{staticClass:"button is-primary",on:{click:t.next}},[t._v("\n                        Next\n                      ")])])])])]),a("div",{staticClass:"columns",style:{display:t.display.message}},[a("div",{staticClass:"column is-8 is-offset-2 box content"},[a("div",{attrs:{align:"center"},domProps:{innerHTML:t._s(t.message)}})])]),a("div",{staticClass:"columns",style:{display:t.display.test}},[a("div",{staticClass:"column is-8 is-offset-2 box content"},[a("div",{attrs:{align:"center"}},[a("h3",[t._v("Please Answer the Following Question")]),a("div",{domProps:{innerHTML:t._s(t.testPrompt)}}),a("div",{staticClass:"block"},[a("b-radio",{attrs:{"native-value":"True"},model:{value:t.radio,callback:function(e){t.radio=e},expression:"radio"}},[t._v("\n                          True\n                      ")]),a("b-radio",{attrs:{"native-value":"False"},model:{value:t.radio,callback:function(e){t.radio=e},expression:"radio"}},[t._v("\n                          False\n                      ")])],1),a("hr"),a("div",{style:{display:t.mTurkDisplay}},[a("p",[t._v("\n                          Please enter an email to be included in a lucky draw\n                          or leave it blank to opt out:\n                      ")]),a("b-field",[a("b-input",{staticStyle:{width:"250px"},attrs:{placeholder:"Your email","icon-pack":"fas",icon:"envelope"},model:{value:t.email,callback:function(e){t.email=e},expression:"email"}})],1)],1),a("div",{staticStyle:{"margin-top":"5px"}},[a("button",{staticClass:"button is-primary",on:{click:t.saveEvaluation}},[t._v("\n                          Submit\n                      ")])])])])])])},I=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("h5",{staticClass:"my-header"},[a("strong",[t._v("How strongly agree are you on the following statements?")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("span",{staticClass:"level-left"},[a("label",{staticClass:"label is-small"},[t._v("Strongly "),a("br"),t._v(" disagree")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("span",{staticClass:"level-right"},[a("label",{staticClass:"label is-small"},[t._v("Strongly "),a("br"),t._v(" agree")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("span",{staticClass:"level-left"},[a("label",{staticClass:"label is-small"},[t._v("Strongly "),a("br"),t._v(" disagree")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("span",{staticClass:"level-right"},[a("label",{staticClass:"label is-small"},[t._v("Strongly "),a("br"),t._v(" agree")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("span",{staticClass:"level-left"},[a("label",{staticClass:"label is-small"},[t._v("Strongly "),a("br"),t._v(" disagree")])])},function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("span",{staticClass:"level-right"},[a("label",{staticClass:"label is-small"},[t._v("Strongly "),a("br"),t._v(" agree")])])}],L=(a("96cf"),a("84b4"),a("3b8d")),N=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},H=[function(){var t=this,e=t.$createElement,a=t._self._c||e;return a("div",{staticClass:"document"},[a("h1",{attrs:{align:"center"}},[t._v("\n        Please Read This Thoroughly Before You Consent!\n    ")]),a("p",[t._v("Your task is to assess the "),a("strong",[t._v("fluency")]),t._v(" of a single summary sentence. There are at most 8 summaries that need to be evaluated. The task should be possible to complete in less than "),a("strong",[t._v("3 minutes")]),t._v(".")]),a("hr"),a("p",[a("strong",[t._v("You have to assess the summary on three metrics:")])]),a("blockquote",[t._v("\n         The summary has a "),a("strong",[t._v("clear reference")]),t._v(".\n    ")]),a("p",[a("strong",[t._v("Meaning:")]),t._v(" All the the referents of nounphrases in this summary are easily identifiable, i.e.: All the nouns, pronouns or personal names are well-specified?.")]),a("blockquote",[t._v("\n        The summary is "),a("strong",[t._v("grammatically")]),t._v(" correct.\n    ")]),a("p",[a("strong",[t._v("Meaning:")]),t._v(" There any no obviously ungrammatical sentences,\n                                e.g.,missing components, unrelated fragments or any other\n                                grammar-related problem that makes the\n                                text difficult to read.")]),a("blockquote",[t._v("\n        The summary has no noticeable "),a("strong",[t._v("formatting problem")])]),a("p",[a("strong",[t._v("Meaning:")]),t._v(" There are no datelines, system-internal\n                          formatting or capitalization errors that can make the reading\n                          of the summary difficult.")]),a("p",[t._v("An example assessment of one bad summary in each category:")]),a("blockquote",[a("strong",[t._v("No Clear Reference")]),a("br"),a("a",{staticClass:"highlight"},[t._v("He")]),t._v(", born 2 May 1975, is a English retired professional footballer and current President of Inter Miami CF since .\n    ")]),a("blockquote",[a("strong",[t._v("Grammatically wrong")]),a("br"),t._v("\n      David Robert Joseph Beckham, born 2 May 1975, "),a("a",{staticClass:"highlight"},[t._v("are a")]),t._v(" English retired professional footballer and current "),a("a",{staticClass:"highlight"},[t._v("current")]),t._v(" President of Inter Miami CF.\n    ")]),a("blockquote",[a("strong",[t._v("Formatting Problem")]),a("br"),t._v("\n      David Robert Joseph Beckham, born "),a("a",{staticClass:"highlight"},[t._v("02051975")]),t._v(", is a English retired "),a("a",{staticClass:"highlight"},[t._v("<UNK>")]),t._v(" footballer and current President of Inter Miami CF.\n    ")]),a("p",[t._v("You will be scoring each summary sentence by stating how strongly you agree or disagree using a slider from scale 1 (strong disagreement) to 100 (strong agreement).")]),a("hr"),a("h4",[a("strong",[t._v("Sanity Check")])]),a("p",[t._v("We have inserted an obviously bad and good fake summaries in between a real summaries. Any submission that failed to recognize the bad and good fake summaries and give them a suitable scores will be "),a("strong",[t._v("rejected.")])]),a("hr"),a("p",[t._v("There is a "),a("strong",[t._v("code")]),t._v(" that you have to copy and paste to Amazon platform at the end of the task.")]),a("p",[t._v("Thank you for reading this")]),a("p",[t._v("\n        Do you consent for this information to be used\n        anonymously for research purposes only?\n    ")])])}],B={name:"LandingInfRefMTurk"},Y=B,J=(a("effe"),Object(l["a"])(Y,N,H,!1,null,"a9c2a35e",null)),W=J.exports,G=a("3b62"),K=a("be08"),Q=a("0e95"),U=a("6f79"),V=a.n(U),X=a("bc3a"),Z=30;function tt(){var t=0;while(this.arr.length<3)t=Math.floor(Math.random()*this.summaries.length)+1,-1===this.arr.indexOf(t)&&this.arr.push(t);this.summaries.splice(this.arr[0],0,{text:this.sanity_summ.best_summary}),this.results.splice(this.arr[0],0,{test:0}),this.summaries.splice(this.arr[1],0,{text:this.sanity_summ.avg_summary}),this.results.splice(this.arr[1],0,{test:0}),this.summaries.splice(this.arr[2],0,{text:this.sanity_summ.worst_summary}),this.results.splice(this.arr[2],0,{test:0}),this.page.total=this.summaries.length}function et(){return at.apply(this,arguments)}function at(){return at=Object(L["a"])(regeneratorRuntime.mark(function t(){var e=this;return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,X.get("/fluency/".concat(this.project_id,"?n=5")).then(function(t){e.sanity_summ=t.data.sanity_summ,e.results=t.data.results,e.summaries=t.data.summaries,e.mturk_code=t.data.mturk_code}).catch(function(){e.showMessage("Server is busy! Please wait 3 minutes and refresh!")});case 2:return console.log(this.arr),t.next=5,tt.call(this);case 5:case"end":return t.stop()}},t,this)})),at.apply(this,arguments)}function st(t){var e=this;X.post("project/save_result/evaluation",t).then(function(){e.$toast.open({message:"Submission successful.",type:"is-success"});var t="";t="1"===e.is_mturk?"<p>Please enter this code:</p>"+"<blockquote>".concat(e.turkCode,"</blockquote>"):"<p>Please refresh the page to do another highlighting. You need to do at least twice to be eligible for the lucky draw.</p>",e.showMessage("<h3>Thank you for submitting!</h3><br/> ".concat(t))}).catch(function(t){e.$toast.open({message:"".concat(t),type:"is-danger"})})}window.onbeforeunload=function(){return"Are you sure you want leave?"};var nt={components:{BIcon:Q["a"],BTooltip:K["a"],BRadio:G["a"],LandingFluency:W,vueSlider:V.a},data:function(){return{arr:[],start_time:0,is_mturk:this.$route.params.mturk,show:!1,summaries:null,sanity_summ:null,results:null,page:{current:1,total:0},timer:{now:Math.trunc((new Date).getTime()/1e3),date:Math.trunc((new Date).getTime()/1e3),isRunning:!0,timer:null},precision:50,recall:50,project_id:this.$route.params.project_id,display:{content:"none",landing:"block",message:"none",test:"none"},message:"",email:"",radio:""}},methods:{prev:function(){1!==this.page.current&&(this.page.current-=1)},next:function(){this.page.current!==this.page.total&&(this.page.current+=1)},showTest:function(){this.display.landing="none",this.display.content="none",this.display.message="none",this.display.test="flex"},showMessage:function(t){this.display.landing="none",this.display.content="none",this.display.message="flex",this.display.test="none",this.message=t},closeLanding:function(){var t=this;this.display.content="flex",this.display.landing="none",window.scrollTo(0,0),this.show=!0,X.get("result/evaluation/".concat(this.summ_status_id)).then(function(e){t.result_id=e.data.result_id}),this.start_time=(new Date).getTime()},saveEvaluation:function(){var t={project_id:this.project_id,status_id:this.summ_status_id,precision:this.precision,recall:this.recall,category:"Informativeness_Ref",mturk_code:"",email:this.email,result_id:this.result_id,opening_time:this.start_time,finished_time:(new Date).getTime()};"1"===this.is_mturk?t.mturk_code=this.turkCode:t.mturk_code=null,""===this.radio?t.validity=!1:"True"===this.radio===this.sanity_answer?t.validity=!0:t.validity=!1,st.call(this,t)}},computed:{summaryText:function(){return this.summaries[this.page.current-1].text},testPrompt:function(){var t="Is the statement below according to the reference sentence is True or False?";return"".concat(t,"<blockquote>").concat(this.sanity_statement,"</blockquote>")},dynamicLanding:function(){return"LandingFluency"},mTurkDisplay:function(){return"0"===this.is_mturk?"block":"none"},timenow:function(){if(!0===this.timer.isRunning){if(this.timer.now-this.timer.date<Z)return"Wait ".concat(Z-(this.timer.now-this.timer.date)," seconds");this.timer.isRunning=!1,window.clearInterval(this.timer.timer)}return"Click to submit"}},mounted:function(){et.call(this)}},it=nt,rt=(a("b730"),Object(l["a"])(it,q,I,!1,null,null,null)),ot=rt.exports;s["default"].use(d["a"]);var lt=new d["a"]({routes:[{path:"/",redirect:{name:"admin"}},{path:"/fluency/:project_id/",name:"fluency",component:ot},{path:"/admin",component:x,children:[{path:"",name:"admin",component:_},{path:"new",component:S,children:[{path:"",name:"new",component:D},{path:"evaluation",name:"newEvaluation",component:D}]}]}]});s["default"].config.productionTip=!1,s["default"].use(i.a),new s["default"]({router:lt,render:function(t){return t(m)}}).$mount("#app")},"5c0b":function(t,e,a){"use strict";var s=a("5e27"),n=a.n(s);n.a},"5e27":function(t,e,a){},"651e":function(t,e,a){},"900b":function(t,e,a){},"9f7d":function(t,e,a){"use strict";var s=a("651e"),n=a.n(s);n.a},b730:function(t,e,a){"use strict";var s=a("900b"),n=a.n(s);n.a},e60f:function(t,e,a){},effe:function(t,e,a){"use strict";var s=a("e60f"),n=a.n(s);n.a}});
//# sourceMappingURL=app.673372c7.js.map