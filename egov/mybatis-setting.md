
# context-datasource.xml

```xml

    <bean id="dataSource" class="org.apache.commons.dbcp.BasicDataSource" destroy-method="close">
        <property name="driverClassName" value="${Globals.db.DriverClassName}"/>
        <property name="url" value="${Globals.db.Url}" />
        <property name="username" value="${Globals.db.UserName}"/>
        <property name="password" value="#{egovEnvCryptoService.getPassword()}"/>
    </bean>

```


# context-mapper.xml


```xml

	<bean id="egov.sqlSession" class="org.mybatis.spring.SqlSessionFactoryBean">
		<property name="dataSource" ref="egov.dataSource"/>
		<property name="configLocation" value="classpath:/egovframework/mapper/config/mapper-config.xml" />

		<property name="mapperLocations">
			<list>
				<value>classpath:/egovframework/mapper/com/**/*_${Globals.DbType}.xml</value>
			</list>
		</property>
	</bean>

    <bean id="egov.sqlSessionTemplate" class="org.mybatis.spring.SqlSessionTemplate">
		<constructor-arg ref="egov.sqlSession"/>
	</bean>
    
    <!-- DB Connection이 한개 일 경우 -->
    <mybatis:scan base-package="egovframework.com">

    <!-- DB Connection이 여러개 일 경우 -->
    <bean id="mapperScannerConfigurer" class="org.mybatis.spring.mapper.MapperScannerConfigurer">
		<property name="basePackage" value="egovframework.com.base,egovframework.com.util"/>
		<property name="sqlSessionFactoryBeanName" value="egov.sqlSession"/>
	</bean>
```
