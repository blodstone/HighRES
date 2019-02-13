<template>
  <div class="container home">
        <div class="columns" :style="{ display: display.landing }">
            <div class="column is-8 is-offset-2 box content">
                <component :is="dynamicLanding"></component>
                <div align="center">
                    <button class="button is-primary is-large" style="margin-bottom: 2rem"
                    v-on:click="closeLanding()">I consent</button>
                </div>
            </div>
        </div>
        <div class="columns" :style="{ display: display.content }">
            <div class="column is-8 is-offset-2 box content">
                <div class="box summary">
                    <div class="content">
                        <h1 align="center">Please don't refresh the page.</h1>
                        <hr>
                        <h5 class="my-header">Assess the following summary.</h5>
                          <div v-if="summaries">
                            <p class="my-summary">
                              {{ summaryText }}
                            </p>
                          </div>
                        <hr>
                        <h5 class="my-header">
                        <strong>How strongly agree are you on the following statements?</strong>
                        </h5>
                        <p>
                            Hover the mouse on top of the
                            <b-tooltip
                                    label="You should treat that all words
                                    in the reference sentence as important,
                                    and words that don't appear in reference as not important.">
                                <b-icon
                                    pack="fas"
                                    icon="info-circle"
                                    size="is-small">
                                </b-icon>
                            </b-tooltip> to see more information.
                        </p>
                        <p class="my-text">
                            <b-tooltip
                                    label="How much trouble did you have identifying
                                    the referents of nounphrases in this summary?
                                    Are there nouns, pronouns or personal names that are
                                    not well-specified?">
                                <b-icon
                                    pack="fas"
                                    icon="info-circle"
                                    size="is-small">
                                </b-icon>
                            </b-tooltip>
                          The summary has a <strong>clear reference</strong>.
                        </p>
                        <div class="level" align="center"
                             style="margin-bottom: 1.8rem; margin-top: 1.8rem;">
                            <span class="level-left">
                                <label class="label is-small">Strongly <br/> disagree</label>
                            </span>
                            <span class="level-item">
                            <vue-slider min=1 max=100 v-model="recall"
                                        v-if="show" width="100%"></vue-slider>
                            </span>
                            <span class="level-right">
                                <label class="label is-small">Strongly <br/> agree</label>
                            </span>
                        </div>
                        <p class="my-text">
                            <b-tooltip
                                    label="Are there any obviously ungrammatical sentences,
                                    e.g.,missing components, unrelated fragments or any other
                                    grammar-related problem that makes the text diffcult toread? ">
                                <b-icon
                                    pack="fas"
                                    icon="info-circle"
                                    size="is-small">
                                </b-icon>
                            </b-tooltip>
                            The summary is <strong>grammatically</strong> correct.</p>
                        <div class="level" align="center"
                             style="margin-bottom: 1.8rem; margin-top: 1.8rem;">
                            <span class="level-left">
                                <label class="label is-small">Strongly <br/> disagree</label>
                            </span>
                            <span class="level-item">
                           <vue-slider min=1 max=100 v-model="precision"
                                       v-if="show" width="100%"></vue-slider>
                            </span>
                            <span class="level-right">
                                <label class="label is-small">Strongly <br/> agree</label>
                            </span>
                        </div>
                        <p class="my-text">
                            <b-tooltip
                              label="Are there any datelines, system-internal
                              formatting orcapitalization errors that can make the reading
                              of the summary difficult?">
                                <b-icon
                                    pack="fas"
                                    icon="info-circle"
                                    size="is-small">
                                </b-icon>
                            </b-tooltip>
                          The summary has no noticeable <strong>formatting problem</strong>.</p>
                        <div class="level" align="center"
                             style="margin-bottom: 1.8rem; margin-top: 1.8rem;">
                            <span class="level-left">
                                <label class="label is-small">Strongly <br/> disagree</label>
                            </span>
                            <span class="level-item">
                           <vue-slider min=1 max=100 v-model="precision"
                                       v-if="show" width="100%"></vue-slider>
                            </span>
                            <span class="level-right">
                                <label class="label is-small">Strongly <br/> agree</label>
                            </span>
                        </div>
                        <div align="center">
                          <button class="button is-primary" v-on:click="prev">
                            Prev
                          </button>
                          <div>
                            {{page.current}}/{{page.total}}
                          </div>
                          <button class="button is-primary" v-on:click="next">
                            Next
                          </button>
                        </div>
                    </div>
                </div>
            </div>
            <!-- eslint-enable -->
        </div>
        <div class="columns" :style="{ display: display.message }">
            <div class="column is-8 is-offset-2 box content">
                <div align="center" v-html="message">
                </div>
            </div>
        </div>
      <div class="columns" :style="{ display: display.test }">
            <div class="column is-8 is-offset-2 box content">
                <div align="center">
                    <h3>Please Answer the Following Question</h3>
                    <div v-html="testPrompt">
                    </div>
                    <div class="block">
                        <b-radio v-model="radio"
                                 native-value="True">
                            True
                        </b-radio>
                        <b-radio v-model="radio"
                                 native-value="False">
                            False
                        </b-radio>
                    </div>
                    <hr/>
                    <div :style="{ display: mTurkDisplay }">
                        <p>
                            Please enter an email to be included in a lucky draw
                            or leave it blank to opt out:
                        </p>
                        <b-field>
                            <b-input v-model="email"
                                     placeholder="Your email"
                                     icon-pack="fas"
                                     icon="envelope" style="width: 250px;"></b-input>
                        </b-field>
                    </div>
                    <div style="margin-top: 5px;">
                        <button class="button is-primary"
                                v-on:click="saveEvaluation">
                            Submit
                        </button>
                    </div>
                </div>
            </div>
        </div>
  </div>
</template>

<script>
/* eslint-disable camelcase */
// @ is an alias to /src
import LandingFluency from '@/views/user/LandingFluency.vue';
import BRadio from 'buefy/src/components/radio/Radio.vue';
import BTooltip from 'buefy/src/components/tooltip/Tooltip.vue';
import BIcon from 'buefy/src/components/icon/Icon.vue';
import vueSlider from 'vue-slider-component';


const axios = require('axios');

const waitTimeForButton = 30;

window.onbeforeunload = () => 'Are you sure you want leave?';

function insertSanitySumms() {
  let r = 0;
  while (this.arr.length < 3) {
    r = Math.floor(Math.random() * this.summaries.length) + 1;
    if (this.arr.indexOf(r) === -1) {
      this.arr.push(r);
    }
  }
  this.summaries.splice(this.arr[0], 0, {
    text: this.sanity_summ.best_summary,
  });
  this.results.splice(this.arr[0], 0, {
    test: 0,
  });
  this.summaries.splice(this.arr[1], 0, {
    text: this.sanity_summ.avg_summary,
  });
  this.results.splice(this.arr[1], 0, {
    test: 0,
  });
  this.summaries.splice(this.arr[2], 0, {
    text: this.sanity_summ.worst_summary,
  });
  this.results.splice(this.arr[2], 0, {
    test: 0,
  });
  this.page.total = this.summaries.length;
}

async function getFile() {
  await axios.get(`/fluency/${this.project_id}?n=5`)
    .then((response) => {
      this.sanity_summ = response.data.sanity_summ;
      this.results = response.data.results;
      this.summaries = response.data.summaries;
      this.mturk_code = response.data.mturk_code;
    })
    .catch(() => {
      this.showMessage('Server is busy! Please wait 3 minutes and refresh!');
    });
  console.log(this.arr);
  await insertSanitySumms.call(this);
}

function sendResult(resultJSON) {
  axios.post('project/save_result/evaluation', resultJSON)
    .then(() => {
      this.$toast.open({
        message: 'Submission successful.',
        type: 'is-success',
      });
      let text = '';
      if (this.is_mturk === '1') {
        text = '<p>Please enter this code:</p>' +
              `<blockquote>${this.turkCode}</blockquote>`;
      } else {
        text = '<p>Please refresh the page to do another highlighting. ' +
          'You need to do at least twice to be eligible for the lucky draw.</p>';
      }
      this.showMessage(`<h3>Thank you for submitting!</h3><br/> ${text}`);
    })
    .catch((error) => {
      this.$toast.open({
        message: `${error}`,
        type: 'is-danger',
      });
    });
}

export default {
  components: {
    BIcon,
    BTooltip,
    BRadio,
    LandingFluency,
    vueSlider,
  },
  data() {
    return {
      arr: [],
      start_time: 0,
      is_mturk: this.$route.params.mturk,
      show: false,
      summaries: null,
      sanity_summ: null,
      results: null,
      page: {
        current: 1,
        total: 0,
      },
      timer: {
        now: Math.trunc(new Date().getTime() / 1000),
        date: Math.trunc(new Date().getTime() / 1000),
        isRunning: true,
        timer: null,
      },
      precision: 50,
      recall: 50,
      project_id: this.$route.params.project_id,
      display: {
        content: 'none',
        landing: 'block',
        message: 'none',
        test: 'none',
      },
      message: '',
      email: '',
      radio: '',
    };
  },
  methods: {
    prev() {
      if (this.page.current !== 1) {
        this.page.current -= 1;
      }
    },
    next() {
      if (this.page.current !== this.page.total) {
        this.page.current += 1;
      }
    },
    showTest() {
      this.display.landing = 'none';
      this.display.content = 'none';
      this.display.message = 'none';
      this.display.test = 'flex';
    },
    showMessage(message) {
      this.display.landing = 'none';
      this.display.content = 'none';
      this.display.message = 'flex';
      this.display.test = 'none';
      this.message = message;
    },
    closeLanding() {
      this.display.content = 'flex';
      this.display.landing = 'none';
      window.scrollTo(0, 0);
      this.show = true;
      axios.get(`result/evaluation/${this.summ_status_id}`)
        .then((response) => {
          this.result_id = response.data.result_id;
        });
      this.start_time = new Date().getTime();
    },
    saveEvaluation() {
      const resultJSON = {
        project_id: this.project_id,
        status_id: this.summ_status_id,
        precision: this.precision,
        recall: this.recall,
        category: 'Informativeness_Ref',
        mturk_code: '',
        email: this.email,
        result_id: this.result_id,
        opening_time: this.start_time,
        finished_time: new Date().getTime(),
      };
      if (this.is_mturk === '1') {
        resultJSON.mturk_code = this.turkCode;
      } else {
        resultJSON.mturk_code = null;
      }
      if (this.radio === '') {
        resultJSON.validity = false;
      } else if ((this.radio === 'True') === this.sanity_answer) {
        resultJSON.validity = true;
      } else {
        resultJSON.validity = false;
      }
      sendResult.call(this, resultJSON);
    },
  },
  computed: {
    summaryText() {
      return this.summaries[this.page.current - 1].text;
    },
    testPrompt() {
      const prompt = 'Is the statement below according to the reference sentence is True or False?';
      return `${prompt}<blockquote>${this.sanity_statement}</blockquote>`;
    },
    dynamicLanding() {
      return 'LandingFluency';
    },
    mTurkDisplay() {
      if (this.is_mturk === '0') {
        return 'block';
      }
      return 'none';
    },
    timenow() {
      if (this.timer.isRunning === true) {
        if ((this.timer.now - this.timer.date) < waitTimeForButton) {
          return `Wait ${waitTimeForButton - (this.timer.now - this.timer.date)} seconds`;
        }
        // eslint-disable-next-line
        this.timer.isRunning = false;
        window.clearInterval(this.timer.timer);
      }
      return 'Click to submit';
    },
  },
  mounted() {
    getFile.call(this);
  },
};
</script>

<style lang="scss">
.home {
  padding-top: 25px;
}
.my-header {
  font-size: 1.1rem;
}
.my-summary{
    font-size: 1.1rem;
}
</style>
