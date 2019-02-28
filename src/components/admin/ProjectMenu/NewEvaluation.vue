<template>
    <div>
        <!--TODO: Add validation-->
        <label class="label">Create a New Project for Manual Evaluation</label>
        <b-field horizontal label="Name" message="Please enter the project name">
            <b-input name="name" expanded v-model="project.name"></b-input>
        </b-field>
        <b-field horizontal label="Category">
            <b-select placeholder="Select evaluation category"
                      v-model="project.category"
                      icon="wrench" icon-pack="fas">
                <option value="Fluency">Fluency</option>
                <option value="Clarity">Clarity</option>
            </b-select>
        </b-field>
        <b-field horizontal label="Dataset" v-if="datasets">
            <b-select placeholder="Select a dataset"
                      v-model="project.dataset" icon="database" icon-pack="fas">
                <option v-for="x in datasets" :value="x" :key="x.name">
                  {{ x.name }}
                </option>
            </b-select>
        </b-field>
        <b-field horizontal label="Summary Group" v-if="project.dataset">
            <b-select multiple native-size="3"
                      placeholder="Select one or more group" v-model="project.summ_group_list">
                <option v-for="x in project.dataset.summ_groups"
                        :value="x" :key="x.name">{{ x.name }}</option>
            </b-select>
        </b-field>
            <!--TODO: Handling error when user input 0-->
        <b-field horizontal label="# of evaluation" message="Number of evaluation per document">
            <b-input name="total_exp_results"
                     v-model.number="project.total_exp_results" type="number"></b-input>
        </b-field>
        <b-field horizontal label="Expire Duration (in min)"
                 message="The time the task has to be finished.">
            <b-input name="expire_duration"
                     v-model.number="project.expire_duration" type="number"></b-input>
        </b-field>
        <b-field horizontal label="# Summaries"
                 message="Number of summaries to be shown at once.">
            <b-input name="n_summaries"
                     v-model.number="project.n_summaries" type="number"></b-input>
        </b-field>
        <button class="button is-primary" v-on:click="createProject">Create Project</button>
    </div>
</template>

<script>
const axios = require('axios');

export default {
  name: 'NewEvaluation',
  data() {
    return {
      datasets: null,
      project: {
        name: '',
        dataset: null,
        summ_group_list: null,
        category: null,
        n_summaries: 5,
        total_exp_results: 1,
        expire_duration: 3,
      },
    };
  },
  methods: {
    createProject() {
      if (this.project.category === 'Fluency') {
        axios.put('admin/fluency', this.project)
          .then(() => {
            this.$toast.open({
              message: 'Project created!',
              type: 'is-success',
            });
            this.$router.push({ name: 'manage' });
          })
          .catch(() => {
            this.$toast.open({
              message: 'Project is not created! Something is wrong',
              type: 'is-danger',
            });
          });
      } else if (this.project.category === 'Clarity') {
        axios.put('admin/clarity', this.project)
          .then(() => {
            this.$toast.open({
              message: 'Project created!',
              type: 'is-success',
            });
            this.$router.push({ name: 'manage' });
          })
          .catch(() => {
            this.$toast.open({
              message: 'Project is not created! Something is wrong',
              type: 'is-danger',
            });
          });
      }
    },
  },
  mounted() {
    axios.get('admin/dataset')
      .then((response) => {
        if (response.status === 404) {
          this.$toast.open({
            message: response.statusText,
            type: 'is-danger',
          });
        } else {
          this.datasets = response.data;
        }
      })
      .catch((error) => {
        this.$toast.open({
          message: `${error}`,
          type: 'is-danger',
        });
      });
  },
};
</script>

<style scoped>

</style>
