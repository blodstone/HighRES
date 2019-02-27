(function(t){function e(e){for(var a,i,o=e[0],l=e[1],c=e[2],m=0,h=[];m<o.length;m++)i=o[m],n[i]&&h.push(n[i][0]),n[i]=0;for(a in l)Object.prototype.hasOwnProperty.call(l,a)&&(t[a]=l[a]);u&&u(e);while(h.length)h.shift()();return r.push.apply(r,c||[]),s()}function s(){for(var t,e=0;e<r.length;e++){for(var s=r[e],a=!0,o=1;o<s.length;o++){var l=s[o];0!==n[l]&&(a=!1)}a&&(r.splice(e--,1),t=i(i.s=s[0]))}return t}var a={},n={app:0},r=[];function i(e){if(a[e])return a[e].exports;var s=a[e]={i:e,l:!1,exports:{}};return t[e].call(s.exports,s,s.exports,i),s.l=!0,s.exports}i.m=t,i.c=a,i.d=function(t,e,s){i.o(t,e)||Object.defineProperty(t,e,{enumerable:!0,get:s})},i.r=function(t){"undefined"!==typeof Symbol&&Symbol.toStringTag&&Object.defineProperty(t,Symbol.toStringTag,{value:"Module"}),Object.defineProperty(t,"__esModule",{value:!0})},i.t=function(t,e){if(1&e&&(t=i(t)),8&e)return t;if(4&e&&"object"===typeof t&&t&&t.__esModule)return t;var s=Object.create(null);if(i.r(s),Object.defineProperty(s,"default",{enumerable:!0,value:t}),2&e&&"string"!=typeof t)for(var a in t)i.d(s,a,function(e){return t[e]}.bind(null,a));return s},i.n=function(t){var e=t&&t.__esModule?function(){return t["default"]}:function(){return t};return i.d(e,"a",e),e},i.o=function(t,e){return Object.prototype.hasOwnProperty.call(t,e)},i.p="/";var o=window["webpackJsonp"]=window["webpackJsonp"]||[],l=o.push.bind(o);o.push=e,o=o.slice();for(var c=0;c<o.length;c++)e(o[c]);var u=l;r.push([0,"chunk-vendors"]),s()})({0:function(t,e,s){t.exports=s("56d7")},"4cf4":function(t,e,s){},"56d7":function(t,e,s){"use strict";s.r(e);s("cadf"),s("551c"),s("f751"),s("097d");var a=s("2b0e"),n=s("8a03"),r=s.n(n),i=(s("5abe"),s("a23f"),function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"clearfix"},[s("router-view")],1)}),o=[],l=(s("5c0b"),s("2877")),c={},u=Object(l["a"])(c,i,o,!1,null,null,null),m=u.exports,h=s("8c4f"),d=function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)},p=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"hero is-primary is-large"},[s("div",{staticClass:"hero-body"},[s("div",{staticClass:"container"},[s("h1",{staticClass:"title"},[t._v("\n        Welcome to HArnESS!\n      ")]),s("h2",{staticClass:"subtitle"},[t._v("\n        An open source manual evaluation software for abstractive summarization!\n      ")])])])])}],v={name:"Home"},f=v,_=(s("9f7d"),Object(l["a"])(f,d,p,!1,null,"c93b39a8",null)),g=_.exports,b=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[s("nav",{staticClass:"navbar",attrs:{role:"navigation","aria-label":"main navigation"}},[s("div",{staticClass:"container is-fluid"},[t._m(0),s("div",{staticClass:"navbar-menu",attrs:{id:"navbarBasicExample"}},[s("div",{staticClass:"navbar-start"},[s("div",{staticClass:"navbar-item has-dropdown is-hoverable"},[s("a",{staticClass:"navbar-link"},[t._v("\n                Projects\n              ")]),s("div",{staticClass:"navbar-dropdown"},[s("router-link",{staticClass:"navbar-item",attrs:{to:{name:"new"}}},[t._v("\n                  New...\n                ")]),s("router-link",{staticClass:"navbar-item",attrs:{to:{name:"manage"}}},[t._v("\n                  Manage...\n                ")])],1)])])])])]),s("router-view")],1)},y=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"navbar-brand"},[s("a",{staticClass:"navbar-item",attrs:{href:"/"}},[t._v("\n          Summ-Eval\n        ")])])}],w={name:"admin"},C=w,x=Object(l["a"])(C,b,y,!1,null,null,null),j=x.exports,k=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"container"},[s("div",{staticClass:"tile is-ancestor"},[s("div",{staticClass:"tile is-parent"},[s("div",{staticClass:"tile is-child tabs"},[s("ul",[s("li",{class:{"is-active":t.isActive.annotation},on:{click:function(e){return t.toggleActive("annotation")}}},[s("router-link",{attrs:{to:{name:"newAnnotation"}}},[t._v("Annotation")])],1),s("li",{class:{"is-active":t.isActive.evaluation},on:{click:function(e){return t.toggleActive("evaluation")}}},[s("router-link",{attrs:{to:{name:"newEvaluation"}}},[t._v("Evaluation")])],1)])])])]),s("div",{staticClass:"tile is-ancestor"},[s("div",{staticClass:"tile is-parent is-5"},[s("div",{staticClass:"tile is-child"},[s("router-view")],1)])])])},T=[],E={name:"NewProject",data:function(){return{isActive:{annotation:!0,evaluation:!1}}},methods:{toggleActive:function(t){"annotation"===t?(this.isActive.annotation=!0,this.isActive.evaluation=!1):"evaluation"===t&&(this.isActive.evaluation=!0,this.isActive.annotation=!1)}}},$=E,P=Object(l["a"])($,k,T,!1,null,"56b7ad3e",null),S=P.exports,M=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",[s("label",{staticClass:"label"},[t._v("Create a New Project for Manual Evaluation")]),s("b-field",{attrs:{horizontal:"",label:"Name",message:"Please enter the project name"}},[s("b-input",{attrs:{name:"name",expanded:""},model:{value:t.project.name,callback:function(e){t.$set(t.project,"name",e)},expression:"project.name"}})],1),s("b-field",{attrs:{horizontal:"",label:"Category"}},[s("b-select",{attrs:{placeholder:"Select evaluation category",icon:"wrench","icon-pack":"fas"},model:{value:t.project.category,callback:function(e){t.$set(t.project,"category",e)},expression:"project.category"}},[s("option",{attrs:{value:"Fluency"}},[t._v("Fluency")])])],1),t.datasets?s("b-field",{attrs:{horizontal:"",label:"Dataset"}},[s("b-select",{attrs:{placeholder:"Select a dataset",icon:"database","icon-pack":"fas"},model:{value:t.project.dataset,callback:function(e){t.$set(t.project,"dataset",e)},expression:"project.dataset"}},t._l(t.datasets,function(e){return s("option",{key:e.name,domProps:{value:e}},[t._v("\n              "+t._s(e.name)+"\n            ")])}),0)],1):t._e(),t.project.dataset?s("b-field",{attrs:{horizontal:"",label:"Summary Group"}},[s("b-select",{attrs:{multiple:"","native-size":"3",placeholder:"Select one or more group"},model:{value:t.project.summ_group_list,callback:function(e){t.$set(t.project,"summ_group_list",e)},expression:"project.summ_group_list"}},t._l(t.project.dataset.summ_groups,function(e){return s("option",{key:e.name,domProps:{value:e}},[t._v(t._s(e.name))])}),0)],1):t._e(),s("b-field",{attrs:{horizontal:"",label:"# of evaluation",message:"Number of evaluation per document"}},[s("b-input",{attrs:{name:"total_exp_results",type:"number"},model:{value:t.project.total_exp_results,callback:function(e){t.$set(t.project,"total_exp_results",t._n(e))},expression:"project.total_exp_results"}})],1),s("b-field",{attrs:{horizontal:"",label:"Expire Duration (in min)",message:"The time the task has to be finished."}},[s("b-input",{attrs:{name:"expire_duration",type:"number"},model:{value:t.project.expire_duration,callback:function(e){t.$set(t.project,"expire_duration",t._n(e))},expression:"project.expire_duration"}})],1),s("b-field",{attrs:{horizontal:"",label:"# Summaries",message:"Number of summaries to be shown at once."}},[s("b-input",{attrs:{name:"n_summaries",type:"number"},model:{value:t.project.n_summaries,callback:function(e){t.$set(t.project,"n_summaries",t._n(e))},expression:"project.n_summaries"}})],1),s("button",{staticClass:"button is-primary",on:{click:t.createProject}},[t._v("Create Project")])],1)},A=[],O=s("bc3a"),z={name:"NewEvaluation",data:function(){return{datasets:null,project:{name:"",dataset:null,summ_group_list:null,category:null,n_summaries:5,total_exp_results:1,expire_duration:3}}},methods:{createProject:function(){var t=this;O.put("admin/fluency",this.project).then(function(){t.$toast.open({message:"Project created!",type:"is-success"}),t.$router.push({name:"manage"})}).catch(function(){t.$toast.open({message:"Project is not created! Something is wrong",type:"is-danger"})})}},mounted:function(){var t=this;O.get("admin/dataset").then(function(e){404===e.status?t.$toast.open({message:e.statusText,type:"is-danger"}):t.datasets=e.data}).catch(function(e){t.$toast.open({message:"".concat(e),type:"is-danger"})})}},R=z,q=Object(l["a"])(R,M,A,!1,null,"7934ba00",null),D=q.exports,L=function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"container home"},[s("div",{staticClass:"columns",style:{display:t.display.landing}},[s("div",{staticClass:"column is-8 is-offset-2 box content"},[s(t.dynamicLanding,{tag:"component"}),s("div",{attrs:{align:"center"}},[s("button",{staticClass:"button is-primary is-large",staticStyle:{"margin-bottom":"2rem"},on:{click:function(e){return t.closeLanding()}}},[t._v("I consent")])])],1)]),s("div",{staticClass:"columns",style:{display:t.display.content}},[s("div",{staticClass:"column is-8 is-offset-2 box content"},[s("div",{staticClass:"box summary"},[s("div",{staticClass:"content"},[s("h1",{attrs:{align:"center"}},[t._v("Please don't refresh the page.")]),s("hr"),s("h5",{staticClass:"my-header"},[t._v("Assess the following summary.")]),t.res_sums?s("div",[s("p",{staticClass:"my-summary"},[t._v("\n                            "+t._s(t.summaryText)+"\n                          ")])]):t._e(),s("hr"),t._m(0),s("p",[t._v("\n                          Hover the mouse on top of the\n                          "),s("b-tooltip",{attrs:{label:"Don't forget to enter the m_turk code\n                                  at the end of the session."}},[s("b-icon",{attrs:{pack:"fas",icon:"info-circle",size:"is-small"}})],1),t._v(" to see more information.\n                      ")],1),s("p",{staticClass:"my-text"},[s("b-tooltip",{attrs:{label:"There should be no difficulties in\n                                  identifying the referents of the noun phrases\n                                  (every noun/place/event should be well-specified)\n                                  or understanding the meaning of the sentence."}},[s("b-icon",{attrs:{pack:"fas",icon:"info-circle",size:"is-small"}})],1),t._v("\n                        The summary is a "),s("strong",[t._v("clear")]),t._v(".\n                      ")],1),s("div",{staticClass:"level",staticStyle:{"margin-bottom":"1.8rem","margin-top":"1.8rem"},attrs:{align:"center"}},[t._m(1),s("span",{staticClass:"level-item"},[t.show?s("vue-slider",{attrs:{min:1,max:100,width:"100%"},model:{value:t.res_sums[t.page.current-1].result.clarity,callback:function(e){t.$set(t.res_sums[t.page.current-1].result,"clarity",e)},expression:"res_sums[page.current - 1].result.clarity"}}):t._e()],1),t._m(2)]),s("p",{staticClass:"my-text"},[s("b-tooltip",{attrs:{label:"The summary should sound natural\n                                  and has no grammar-related problem that\n                                  makes the text difficult to read. "}},[s("b-icon",{attrs:{pack:"fas",icon:"info-circle",size:"is-small"}})],1),t._v("\n                          The summary is "),s("strong",[t._v("fluent")]),t._v(".")],1),s("div",{staticClass:"level",staticStyle:{"margin-bottom":"1.8rem","margin-top":"1.8rem"},attrs:{align:"center"}},[t._m(3),s("span",{staticClass:"level-item"},[t.show?s("vue-slider",{attrs:{min:1,max:100,width:"100%"},model:{value:t.res_sums[t.page.current-1].result.fluency,callback:function(e){t.$set(t.res_sums[t.page.current-1].result,"fluency",e)},expression:"res_sums[page.current - 1].result.fluency"}}):t._e()],1),t._m(4)]),s("div",{staticClass:"level column-5"},[s("div",{staticClass:"level-item"},[s("button",{staticClass:"button is-primary",on:{click:t.prev}},[t._v("\n                            Prev\n                          ")])]),s("div",{staticClass:"level-item"},[s("strong",[t._v("\n                            "+t._s(t.page.current)+"/"+t._s(t.page.total)+"\n                          ")])]),s("div",{staticClass:"level-item"},[s("button",{staticClass:"button is-primary",on:{click:t.next}},[t._v("\n                            Next\n                          ")])])]),s("div",{attrs:{align:"center"}},[s("button",{staticClass:"button is-primary",on:{click:t.saveEvaluation}},[t._v("\n                          Finish\n                        ")])])])])])]),s("div",{staticClass:"columns",style:{display:t.display.message}},[s("div",{staticClass:"column is-8 is-offset-2 box content"},[s("div",{attrs:{align:"center"},domProps:{innerHTML:t._s(t.message)}})])])])},F=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("h5",{staticClass:"my-header"},[s("strong",[t._v("How strongly agree are you on the following statements?")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("span",{staticClass:"level-left"},[s("label",{staticClass:"label is-small"},[t._v("Strongly "),s("br"),t._v(" disagree")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("span",{staticClass:"level-right"},[s("label",{staticClass:"label is-small"},[t._v("Strongly "),s("br"),t._v(" agree")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("span",{staticClass:"level-left"},[s("label",{staticClass:"label is-small"},[t._v("Strongly "),s("br"),t._v(" disagree")])])},function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("span",{staticClass:"level-right"},[s("label",{staticClass:"label is-small"},[t._v("Strongly "),s("br"),t._v(" agree")])])}],N=(s("96cf"),s("84b4"),s("3b8d")),I=(s("55dd"),function(){var t=this,e=t.$createElement;t._self._c;return t._m(0)}),B=[function(){var t=this,e=t.$createElement,s=t._self._c||e;return s("div",{staticClass:"document"},[s("h1",{attrs:{align:"center"}},[t._v("\n        Please Read This Thoroughly Before You Consent!\n    ")]),s("p",[t._v("Your task is to assess the "),s("strong",[t._v("quality")]),t._v(" of an English summary sentence. There are at most 8 sentences that need to be evaluated separately. The task should be possible to complete in less than "),s("strong",[t._v("3 minutes")]),t._v(".")]),s("hr"),s("p",[s("strong",[t._v("You have to assess a summary on two aspects:")])]),s("blockquote",[t._v("\n      1. The "),s("strong",[t._v("clarity")]),t._v(" of the summary.\n    ")]),s("p",[s("strong",[t._v("Explanation:")]),t._v(" The summary has to be easy to be understood. There should be no difficulties in identifying the referents of the noun phrases (every noun/place/event should be well-specified) or understanding the meaning of the sentence. ")]),s("blockquote",[t._v("\n      2. The "),s("strong",[t._v("fluency")]),t._v(" of the summary.\n    ")]),s("p",[s("strong",[t._v("Explanation:")]),t._v(" The summary should sound natural and has no grammar-related problem that makes the text difficult to read.")]),s("p",[t._v("The following are assessment of a bad summary according to each aspect:")]),s("blockquote",[s("strong",[t._v("Lack of clarity")]),s("br"),s("a",{staticClass:"highlight"},[t._v("He")]),t._v(", born 2 May 1975, is a English retired professional footballer and current President of Inter Miami CF since .\n      "),s("p",[s("strong",[t._v("Explanation:")]),t._v(" The person that is higlighted is not well-specified which reduce the clarity of the sentence.")])]),s("blockquote",[s("strong",[t._v("Grammatically wrong")]),s("br"),t._v("\n      David Robert Joseph Beckham, born 2 May 1975, "),s("a",{staticClass:"highlight"},[t._v("are a")]),t._v(" English retired professional footballer and current "),s("a",{staticClass:"highlight"},[t._v("current")]),t._v(" President of Inter Miami CF.\n     "),s("p",[s("strong",[t._v("Explanation:")]),t._v(" The highlighted words are grammatically wrong.")])]),s("p",[t._v("You will be scoring each summary sentence by stating how strongly you agree or disagree using a slider from scale 1 (strong disagreement) to 100 (strong agreement).")]),s("hr"),s("h4",[s("strong",[t._v("Sanity Check")])]),s("p",[t._v("We have inserted "),s("strong",[t._v("an obviously bad, mediocre and good summaries")]),t._v(" in between a real summaries. A bad summary has many grammatical mistakes and isn't fluent at all, a mediocre summary has some grammatical mistakes but still understandable, while a good summary has no grammatical mistakes and is fluent.")]),s("p",[t._v("Any submission that failed to recognize the bad, mediocre and good summaries with a suitable scores (bad < medium < good) will be "),s("strong",[t._v("rejected.")])]),s("hr"),s("p",[t._v("There is a "),s("strong",[t._v("code")]),t._v(" that you have to copy and paste to Amazon platform at the end of the task.")]),s("p",[t._v("Thank you for reading this")]),s("p",[t._v("\n        Do you consent for this information to be used\n        anonymously for research purposes only?\n    ")])])}],H={name:"LandingInfRefMTurk"},Y=H,J=(s("8777"),Object(l["a"])(Y,I,B,!1,null,"4a9943dd",null)),W=J.exports,G=s("3b62"),K=s("be08"),Q=s("0e95"),U=s("6f79"),V=s.n(U),X=s("bc3a"),Z=30;function tt(){var t=0;while(this.arr.length<3)t=Math.floor(Math.random()*this.res_sums.length)+1,-1===this.arr.indexOf(t)&&this.arr.push(t);this.arr.sort(),this.res_sums.splice(this.arr[0],0,{result:{clarity:50,fluency:50,type:"best"},summary:{text:this.sanity_summ.best_summary}}),this.res_sums.splice(this.arr[1],0,{result:{clarity:50,fluency:50,type:"avg"},summary:{text:this.sanity_summ.avg_summary}}),this.res_sums.splice(this.arr[2],0,{result:{clarity:50,fluency:50,type:"worst"},summary:{text:this.sanity_summ.worst_summary}}),this.page.total=this.res_sums.length}function et(){return st.apply(this,arguments)}function st(){return st=Object(N["a"])(regeneratorRuntime.mark(function t(){var e=this;return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:return t.next=2,X.get("/fluency/".concat(this.project_id)).then(function(t){e.sanity_summ=t.data.sanity_summ,e.res_sums=t.data.res_sums,e.proj_status=t.data.proj_status}).then(function(){tt.call(e)}).catch(function(){e.showMessage("Server is busy! Please wait 3 minutes and refresh!")});case 2:case"end":return t.stop()}},t,this)})),st.apply(this,arguments)}function at(){for(var t=this,e=[],s=0;s<this.res_sums.length;s+=1)e.push(this.res_sums[s].result);X.post("fluency",{results:e,proj_status:this.proj_status}).then(function(){t.$toast.open({message:"Submission successful.",type:"is-success"});var e="<p>Please enter this code:</p>"+"<blockquote>".concat(t.proj_status.mturk_code,"</blockquote>");t.showMessage("<h3>Thank you for submitting!</h3><br/> ".concat(e))}).catch(function(e){t.$toast.open({message:"".concat(e),type:"is-danger"})})}window.onbeforeunload=function(){return"Are you sure you want leave?"};var nt={components:{BIcon:Q["a"],BTooltip:K["a"],BRadio:G["a"],LandingFluency:W,vueSlider:V.a},data:function(){return{max:100,min:1,arr:[],start_time:0,show:!1,res_sums:null,proj_status:null,sanity_summ:null,page:{current:1,total:0},timer:{now:Math.trunc((new Date).getTime()/1e3),date:Math.trunc((new Date).getTime()/1e3),isRunning:!0,timer:null},project_id:this.$route.params.project_id,display:{content:"none",landing:"block",message:"none",test:"none"},message:"",email:"",radio:""}},methods:{prev:function(){1!==this.page.current&&(this.page.current-=1)},next:function(){this.page.current!==this.page.total&&(this.page.current+=1)},showTest:function(){this.display.landing="none",this.display.content="none",this.display.message="none",this.display.test="flex"},showMessage:function(t){this.display.landing="none",this.display.content="none",this.display.message="flex",this.display.test="none",this.message=t},closeLanding:function(){this.display.content="flex",this.display.landing="none",window.scrollTo(0,0),this.show=!0,this.start_time=(new Date).getTime()},saveEvaluation:function(){this.res_sums[this.arr[2]].result.fluency<this.res_sums[this.arr[0]].result.fluency&&this.res_sums[this.arr[2]].result.fluency<this.res_sums[this.arr[1]].result.fluency&&(this.proj_status.validity=!0,this.proj_status.finished=!0),this.proj_status.finished=!1,this.proj_status.is_active=!1,this.res_sums.splice(this.arr[2],1),this.res_sums.splice(this.arr[1],1),this.res_sums.splice(this.arr[0],1),at.call(this)}},computed:{summaryText:function(){return this.res_sums[this.page.current-1].summary.text},testPrompt:function(){var t="Is the statement below according to the reference sentence is True or False?";return"".concat(t,"<blockquote>").concat(this.sanity_statement,"</blockquote>")},dynamicLanding:function(){return"LandingFluency"},mTurkDisplay:function(){return"0"===this.is_mturk?"block":"none"},timenow:function(){if(!0===this.timer.isRunning){if(this.timer.now-this.timer.date<Z)return"Wait ".concat(Z-(this.timer.now-this.timer.date)," seconds");this.timer.isRunning=!1,window.clearInterval(this.timer.timer)}return"Click to submit"}},beforeMount:function(){var t=Object(N["a"])(regeneratorRuntime.mark(function t(){return regeneratorRuntime.wrap(function(t){while(1)switch(t.prev=t.next){case 0:et.call(this);case 1:case"end":return t.stop()}},t,this)}));function e(){return t.apply(this,arguments)}return e}()},rt=nt,it=(s("b730"),Object(l["a"])(rt,L,F,!1,null,null,null)),ot=it.exports;a["default"].use(h["a"]);var lt=new h["a"]({routes:[{path:"/",redirect:{name:"admin"}},{path:"/fluency/:project_id/",name:"fluency",component:ot},{path:"/admin",component:j,children:[{path:"",name:"admin",component:g},{path:"new",component:S,children:[{path:"",name:"new",component:D},{path:"evaluation",name:"newEvaluation",component:D}]}]}]});a["default"].config.productionTip=!1,a["default"].use(r.a),new a["default"]({router:lt,render:function(t){return t(m)}}).$mount("#app")},"5c0b":function(t,e,s){"use strict";var a=s("5e27"),n=s.n(a);n.a},"5e27":function(t,e,s){},"651e":function(t,e,s){},8777:function(t,e,s){"use strict";var a=s("4cf4"),n=s.n(a);n.a},"900b":function(t,e,s){},"9f7d":function(t,e,s){"use strict";var a=s("651e"),n=s.n(a);n.a},b730:function(t,e,s){"use strict";var a=s("900b"),n=s.n(a);n.a}});
//# sourceMappingURL=app.51f3e91f.js.map