<!--
Main Admin page (load Home as its component)
-->
<template>
  <div>
    <nav class="navbar" role="navigation" aria-label="main navigation">
      <div class="container is-fluid">
        <div class="navbar-brand">
          <a href="/" class="navbar-item">
            Harness
          </a>
        </div>
          <div id="navbarBasicExample" class="navbar-menu">
            <div class="navbar-start">
              <div class="navbar-item has-dropdown is-hoverable">
                <a class="navbar-link">
                  Projects
                </a>
                <div class="navbar-dropdown">
                  <router-link class="navbar-item" :to="{name: 'new'}">
                    New...
                  </router-link>
                  <router-link class="navbar-item" :to="{name: 'manage'}">
                    Manage...
                  </router-link>
                </div>
              </div>
            </div>
          </div>
        </div>
    </nav>
    <router-view></router-view>
  </div>
</template>

<script lang="ts">
import { Vue, Component } from 'vue-property-decorator';

@Component
export default class Admin extends Vue {}
</script>
