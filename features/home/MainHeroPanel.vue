<template>
  <HomePanel colSpan="12" rowSpan="10" to="course">
    <template v-slot:bg>
      <Duotone color="Pink">
        <img alt="Students learning to code." src="~/assets/img/upleveled_4_2bit.avif"/>
      </Duotone>
    </template>

    <template v-slot:top>
      <CoreButton size="S" variant="secondary">
        231 Chapel Street, Prahran
      </CoreButton>
      <CoreButton size="S" variant="secondary">
        September 18 - December 8
      </CoreButton>
    </template>

    <Heading font="PassionOne" type="h1">THE EARTH<br/>IS SQUARE</Heading>
    <Heading type="h4">WEB DEVELOPMENT BOOTCAMP</Heading>

    <template v-slot:bot>
      <CoreButton size="L" variant="secondary">
        Enrolments Open
      </CoreButton>
    </template>
  </HomePanel>
</template>