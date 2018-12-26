<template>
  <div>
    <nav-header></nav-header>
    <div style="background-color: #e9ecef;">
      <div class="container" style="background-color: #e9ecef;">
        <ol class="breadcrumb">
          <li class="breadcrumb-item"><a href="#">首页</a></li>
          <li class="breadcrumb-item"><a href="#">版本说明书</a></li>
          <li class="breadcrumb-item"><a href="#">iOS</a></li>
          <li class="breadcrumb-item active"><a href="#">国元</a></li>
          <li class="breadcrumb-item active"><a href="#">测试</a></li>
          <li class="breadcrumb-item active">国元20181212_1测试</li>
        </ol>
      </div>
    </div>
  </div>
</template>

<script>
  import NavHeader from './../components/NavHeader'

  export default {
    name: "Index",
    components: {
      NavHeader
    }
  }
</script>

<style scoped>

</style>
