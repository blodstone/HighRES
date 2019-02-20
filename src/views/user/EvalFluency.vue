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
                          <div v-if="res_sums">
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
                                    label="Don't forget to enter the m_turk code
                                    at the end of the session.">
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
                            <vue-slider :min=1 :max=100
                                        v-model="res_sums[page.current - 1].result.clarity"
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
                                    grammar-related problem that makes the
                                    text difficult to read? ">
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
                           <vue-slider :min=1 :max=100
                                       v-model="res_sums[page.current - 1].result.fluency"
                                       v-if="show" width="100%"></vue-slider>
                            </span>
                            <span class="level-right">
                                <label class="label is-small">Strongly <br/> agree</label>
                            </span>
                        </div>
                        <div class="level column-5">
                          <div class="level-item">
                            <button class="button is-primary" v-on:click="prev">
                              Prev
                            </button>
                          </div>
                          <div class="level-item">
                            <strong>
                              {{page.current}}/{{page.total}}
                            </strong>
                          </div>
                          <div class="level-item">
                            <button class="button is-primary" v-on:click="next">
                              Next
                            </button>
                          </div>
                        </div>
                        <div align="center">
                          <button class="button is-primary" v-on:click="saveEvaluation">
                            Finish
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
    r = Math.floor(Math.random() * this.res_sums.length) + 1;
    if (this.arr.indexOf(r) === -1) {
      this.arr.push(r);
    }
  }
  this.arr.sort();
  this.res_sums.splice(this.arr[0], 0, {
    result: {
      clarity: 50,
      fluency: 50,
      type: 'best',
    },
    summary: {
      text: this.sanity_summ.best_summary,
    },
  });
  this.res_sums.splice(this.arr[1], 0, {
    result: {
      clarity: 50,
      fluency: 50,
      type: 'avg',
    },
    summary: {
      text: this.sanity_summ.avg_summary,
    },
  });
  this.res_sums.splice(this.arr[2], 0, {
    result: {
      clarity: 50,
      fluency: 50,
      type: 'worst',
    },
    summary: {
      text: this.sanity_summ.worst_summary,
    },
  });
  this.page.total = this.res_sums.length;
}

async function getFile() {
  await axios.get(`/fluency/${this.project_id}`)
    .then((response) => {
      this.sanity_summ = response.data.sanity_summ;
      this.res_sums = response.data.res_sums;
      this.proj_status = response.data.proj_status;
    })
    .then(() => {
      insertSanitySumms.call(this);
    })
    .catch(() => {
      this.showMessage('Server is busy! Please wait 3 minutes and refresh!');
    });
}

function sendResult() {
  const results = [];
  for (let i = 0; i < this.res_sums.length; i += 1) {
    results.push(this.res_sums[i].result);
  }
  axios.post('fluency', {
    results,
    proj_status: this.proj_status,
  })
    .then(() => {
      this.$toast.open({
        message: 'Submission successful.',
        type: 'is-success',
      });
      const text = '<p>Please enter this code:</p>' +
              `<blockquote>${this.proj_status.mturk_code}</blockquote>`;
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
      max: 100,
      min: 1,
      arr: [],
      start_time: 0,
      show: false,
      res_sums: null,
      proj_status: null,
      sanity_summ: null,
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
      this.start_time = new Date().getTime();
    },
    saveEvaluation() {
      if (this.res_sums[this.arr[2]].result.fluency <
        this.res_sums[this.arr[0]].result.fluency &&
        this.res_sums[this.arr[2]].result.fluency <
        this.res_sums[this.arr[1]].result.fluency) {
        this.proj_status.validity = true;
        this.proj_status.finished = true;
      }
      this.proj_status.finished = false;
      this.proj_status.is_active = false;
      this.res_sums.splice(this.arr[2], 1);
      this.res_sums.splice(this.arr[1], 1);
      this.res_sums.splice(this.arr[0], 1);
      sendResult.call(this);
    },
  },
  computed: {
    summaryText() {
      return this.res_sums[this.page.current - 1].summary.text;
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
  beforeMount: async function onBeforeMount() {
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
