<template>
  <div>
    <!--TODO: Add validation-->
    <label class="label">Create a New Project for Manual Evaluation</label>
    <b-field horizontal label="Name" message="Please enter the project name">
      <b-input name="name" expanded v-model="project.name"></b-input>
    </b-field>
    <b-field horizontal label="Category">
      <b-select placeholder="Select evaluation category" v-model="project.category"
                icon="wrench" icon-pack="fas">
        <option value="Fluency">Fluency</option>
      </b-select>
    </b-field>
    <b-field horizontal label="Dataset">
      <b-select placeholder="Select a dataset"
                v-model="project.dataset_name" icon="database" icon-pack="fas">
        <option v-for="name in names.dataset" :value="name" :key="name">{{ name }}</option>
      </b-select>
    </b-field>
    <b-field horizontal label="Summary Group">
      <b-select placeholder="Select a summary group" v-model="project.summ_group_name"
                icon="file" icon-pack="fas">
        <option v-for="name in names.summ_group"
                :value="name" :key="name">{{ name }}</option>
      </b-select>
    </b-field>
    <!--TODO: Handling error when user input 0-->
    <b-field horizontal label="# of evaluation" message="Number of evaluation per document">
      <b-input name="total_exp_results"
               v-model.number="project.total_exp_results" type="number"></b-input>
    </b-field>
    <button class="button is-primary" v-on:click="createProject">Create Project</button>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';
import axios from 'axios';

@Component
export default class NewEvaluation extends Vue {
  public names = {
      dataset: [] as object[],
      summ_group: [] as object[],
  };

  public project = {
      name: '' as  string,
      dataset_name: '' as null | string,
      sum_group_name: '' as null | string,
      category: null as null | object,
      total_exp_results: 1 as number,
  };

  public createProject() {
      axios.post('/project/evaluation', this.project)
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

  public mounted() {
    axios.get('dataset')
        .then((response) => {
            if (response.status === 204) {
                this.$toast.open({
                    message: 'There is no dataset in database. Please insert dataset first!',
                    type: 'is-danger',
                });
            } else {
                this.names.dataset = response.data.names;
            }
        })
        .catch((error) => {
            this.$toast.open({
                message: `${error}`,
                type: 'is-danger',
            });
        });
    axios.get('summ_group')
        .then((response) => {
            if (response.status === 204) {
                this.$toast.open({
                    message: 'There is no summary group in database. Please insert summary group first!',
                    type: 'is-danger',
                });
            } else {
                this.names.summ_group = response.data.names;
            }
        })
        .catch((error) => {
            this.$toast.open({
                message: `${error}`,
                type: 'is-danger',
            });
        });
  }
}
</script>

<style scoped>

</style>
