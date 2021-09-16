package ${PACKAGE}.entity;

import lombok.Getter;

import javax.persistence.Entity;
import javax.persistence.Id;

@Entity(name = "${ROUTE_NAME}")
@Getter
public class ${SINGLE_ROUTE_NAME_CAPITALIZE}Entity {

    @Id
    private int id;

}