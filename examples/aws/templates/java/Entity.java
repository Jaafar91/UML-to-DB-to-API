package ${PACKAGE}.entity;

import lombok.*;
import javax.persistence.Entity;
import javax.persistence.Id;
import java.util.Date;

@Entity(name = "${ROUTE_NAME}")
@Setter
@Getter
@Builder
@NoArgsConstructor
@AllArgsConstructor
public class ${SINGLE_ROUTE_NAME_CAPITALIZE}Entity {

    @Id
    ${ENTITY_ID}

    ${ENTITY_OTHER_COLUMNS}

}