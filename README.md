# Google 뉴스를 스크래핑하는 프로젝트입니다.

# 고민

1. python 구조 설계 과정에서 코드 작성하기 전에 머릿속으로 그리는 과정 어려움

   > 지금은 코드 작성해보고 과정을 따라가면서 유효성을 검증하고 피드백하는 과정으로 진행

# challenge 문제 정답 피드백

1. def 함수 내에 동일한 함수를 사용하여 함수를 재시작함으로써 일종의 무한 loop을 생성할 수 있음

   > 이런 식으로 loop구조를 만들어 주면 한 번의 return만을 통해 loop을 탈출하기가 쉬워짐

2. 함수1이 함수2를 요청하도록, 함수2가 함수1을 요청하도록 말단부분에 작성해주면 두 함수가 연결되어 서로가 서로를 요청할 수 있음

   > 일종의 주기가 2인 loop을 만들 수 있음

3. user의 정보를 받아오는 함수(함수1)와 실제로 정보를 처리하는 함수(함수2)를 구분해서 작성하자

   > 함수1에서 user에게 정보를 잘 못 받아오면 함수1을 함수1의 내부에서 다시 요청함으로써 loop을 구성할 수 있기 때문

4. 함수 내부에서 같은 함수를 호출해서 loop을 구성할 때에는 항상 return 시켜 주어야 한다.

   > return 시키지 않으면, 함수의 종료 후에 (호출한 point 이후부터) 함수가 다시 수행되는데 이때 문제가 발생한다.

   > 대표적으로는, UnboundLocalError: local variable referenced before assignment 가 있다.

5. repl.it 에서 너무 많은 데이터를 관리하려고 하면 console창이 죽어버리는 경우가 있다.

   > 변화되어도 상관없는 데이터들은 생성될 때마다 특정 과정을 바로 수행해서 데이터의 크기를 줄이는 과정 필요

   > csv 파일을 생성하는 function을 loop안에서 수행해서 데이터 크기 줄이는 과정도 필요

6. 이상적인 코드와 비교했을때, 결과는 동일하지만 내 코드가 훨씬 장황한 경우가 많다.

   > 구현 과정에서 더 깔끔하게 작성할 수 없는지 계속 스스로 피드백하는 과정 필요
