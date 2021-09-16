package ${PACKAGE}.entity;

import lombok.Getter;

import javax.persistence.Entity;
import javax.persistence.Id;
import java.util.Date;

@Entity(name = "${ROUTE_NAME}")
@Getter
public class ${SINGLE_ROUTE_NAME_CAPITALIZE}Entity {

    @Id
    ${ENTITY_ID}

    ${ENTITY_OTHER_COLUMNS}

}